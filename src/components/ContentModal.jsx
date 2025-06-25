import React, { useState, useEffect, useRef } from 'react';
import { courseForms } from '../data/courseForms';

export const ContentModal = ({ heading, onClose }) => {
  const isDefault = heading === 'Assistant';
  const formConfig = courseForms[heading] || [];
  const [formData, setFormData] = useState({});
  const [apiResponse, setApiResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const responseRef = useRef(null);
  const formRef = useRef(null);
  const [selectedPoint, setSelectedPoint] = useState('');

  useEffect(() => {
    setFormData({});
    const saved = localStorage.getItem(`response_${heading}`);
    setApiResponse(saved ? JSON.parse(saved) : null);
    const selected = localStorage.getItem(`selected_${heading}`);
    setSelectedPoint(selected || '');
  }, [heading]);

  useEffect(() => {
    const autofillMap = {
      'Market Research': ['niche'],
    };
    if (selectedPoint && autofillMap[heading]) {
      const newFormData = { ...formData };
      autofillMap[heading].forEach(fieldName => {
        newFormData[fieldName] = selectedPoint;
      });
      setFormData(newFormData);
    }
  }, [selectedPoint, formConfig, heading]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setApiResponse(null);
    let url = '';
    let payload = {};
    if (heading === 'Choosing a Niche') {
      url = 'http://116.202.210.102:8111/module1/choosing-niche';
      payload = {
        target_group: formData.targetGroup,
        problem: formData.problem,
        benefit: formData.benefit,
      };
    } else if (heading === 'Market Research') {
      url = 'http://116.202.210.102:8111/module1/market-research';
      payload = {
        niche: formData.niche,
      };
    } else {
      setApiResponse({ info: 'API integration for this form is not implemented yet.' });
      setLoading(false);
      return;
    }
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });
      const data = await response.json();
      setApiResponse(data);
      localStorage.setItem(`response_${heading}`, JSON.stringify(data));
      setLoading(false);
      setTimeout(() => {
        if (responseRef.current) {
          responseRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }, 100);
    } catch (error) {
      setApiResponse({ error: 'API call failed' });
      setLoading(false);
    }
  };

  const handleRegenerate = () => {
    setFormData({});
    setTimeout(() => {
      if (formRef.current) {
        formRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 100);
  };

  // Double click handler for response points
  const handlePointDoubleClick = (point) => {
    setSelectedPoint(point);
    localStorage.setItem(`selected_${heading}`, point);
    alert('Your selection has been saved!');
  };

  return (
    <div className="fixed bottom-20 right-6 z-50 w-[400px] h-[450px] bg-white rounded-xl shadow-2xl flex flex-col border border-gray-200">
      <div className="flex items-center justify-between px-4 py-3 border-b border-gray-100 bg-[#5035f6] rounded-t-xl">
        <h2 className="text-[15px] font-bold text-white">{isDefault ? 'Assistant' : heading}</h2>
        <button
          className="text-white hover:text-gray-200 text-2xl font-bold ml-2 cursor-pointer"
          onClick={onClose}
          title="Close"
        >
          &times;
        </button>
      </div>
      <div className="flex-1 p-4 overflow-y-auto">
        {isDefault ? (
          <p className="text-gray-700 text-lg mt-2">Please select a course from the sidebar to begin.</p>
        ) : (
          <form ref={formRef} onSubmit={handleSubmit}>
            {formConfig.map(field => (
              <div key={field.name} className="mb-4">
                <label className="block text-gray-700 mb-1">{field.label}</label>
                <input
                  type={field.type}
                  name={field.name}
                  value={formData[field.name] || ''}
                  onChange={handleChange}
                  className="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-[#5035f6]"
                />
              </div>
            ))}
            {formConfig.length > 0 && (
              <button type="submit" className="w-full bg-[#5035f6] text-white py-2 rounded hover:bg-[#3d28b1] cursor-pointer">Submit</button>
            )}
          </form>
        )}
        {loading && (
          <div className="mt-4 flex justify-center items-center">
            <div className="loader border-4 border-gray-200 border-t-[#5035f6] rounded-full w-8 h-8 animate-spin"></div>
          </div>
        )}
        {apiResponse && (
          <div ref={responseRef} className="mt-4 p-3 bg-gray-100 rounded text-sm text-gray-800 border border-gray-200">
            {apiResponse.result ? (
              <>
                <div className="font-bold mb-2">Result:</div>
                <ol className="list-decimal pl-5 space-y-2">
                  {Array.isArray(apiResponse.result)
                    ? apiResponse.result.map((item, idx) => (
                        <li key={idx} onDoubleClick={() => handlePointDoubleClick(item.replace(/^\d+\.\s*/, ''))} className="cursor-pointer">{item.replace(/^\d+\.\s*/, '')}</li>
                      ))
                    : apiResponse.result.split(/\n\d+\./).filter(Boolean).map((item, idx) => (
                        <li key={idx} onDoubleClick={() => handlePointDoubleClick(item.trim().replace(/^\d+\.\s*/, ''))} className="cursor-pointer">{item.trim().replace(/^\d+\.\s*/, '')}</li>
                      ))}
                </ol>
                {selectedPoint && (
                  <div className="mt-4 p-2 bg-green-100 border border-green-300 rounded text-green-800 text-sm">
                    <b>Selected:</b> {selectedPoint}
                  </div>
                )}
              </>
            ) : apiResponse.error ? (
              <div className="text-red-600">{apiResponse.error}</div>
            ) : apiResponse.info ? (
              <div>{apiResponse.info}</div>
            ) : null}
            <button
              className="mt-4 px-4 py-1 bg-[#5035f6] text-white rounded hover:bg-[#3d28b1]"
              onClick={handleRegenerate}
            >
              Regenerate
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

