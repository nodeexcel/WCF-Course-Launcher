import React, { useState, useRef, useEffect } from 'react';
import { courseForms } from '../../data/courseForms';
import toast, { Toaster } from 'react-hot-toast';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const SubscriptionProductModal = ({ onClose }) => {
  const formConfig = courseForms['Subscription Product'] || [];
  const [formData, setFormData] = useState({});
  const [apiResponse, setApiResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const responseRef = useRef(null);
  const formRef = useRef(null);

  useEffect(() => {
    // Autofill 'niche' from localStorage if available (from Choosing a Niche or Market Research)
    const selectedNiche = localStorage.getItem('selected_Choosing a Niche') || localStorage.getItem('selected_Market Research') || '';
    if (selectedNiche) {
      setFormData(prev => ({ ...prev, niche: selectedNiche }));
    }
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setApiResponse(null);
    try {
      // Map camelCase formData to snake_case for API
      const payload = {
        product_title: formData.productTitle || '',
        key_promise: formData.keyPromise || '',
        niche: formData.niche || '',
        main_problem: formData.mainProblem || '',
        audience: formData.audience || '',
        current_skills: formData.currentSkills || '',
        target_skills: formData.targetSkills || '',
        pillar_1: formData.pillar1 || '',
        pillar_2: formData.pillar2 || '',
        pillar_3: formData.pillar3 || '',
        pillar_4: formData.pillar4 || '',
        general_topic: formData.generalTopic || ''
      };
      const response = await fetch(`${API_BASE_URL}/module2/subscription-product-structure`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });
      const data = await response.json();
      if (!response.ok) {
        setApiResponse({ error: data.error || 'Something went wrong.' });
      } else {
        setApiResponse(data);
      }
    } catch (error) {
      setApiResponse({ error: error.message || 'Network error.' });
    }
    setLoading(false);
  };

  const handleRegenerate = () => {
    setFormData({});
    setTimeout(() => {
      if (formRef.current) {
        formRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 100);
  };

  return (
    <div className="fixed bottom-20 right-6 z-50 w-[400px] h-[450px] bg-white rounded-xl shadow-2xl flex flex-col border border-gray-200">
      <Toaster position="top-right" />
      <div className="flex items-center justify-between px-4 py-3 border-b border-gray-100 bg-[#5035f6] rounded-t-xl">
        <h2 className="text-[15px] font-bold text-white">Subscription Product</h2>
        <button
          className="text-white hover:text-gray-200 text-2xl font-bold ml-2 cursor-pointer"
          onClick={onClose}
          title="Close"
        >
          &times;
        </button>
      </div>
      <div className="flex-1 p-4 overflow-y-auto">
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
                        <li key={idx}>{item.replace(/^\d+\.\s*/, '')}</li>
                      ))
                    : apiResponse.result.split(/\n\d+\./).filter(Boolean).map((item, idx) => (
                        <li key={idx}>{item.trim().replace(/^\d+\.\s*/, '')}</li>
                      ))}
                </ol>
              </>
            ) : apiResponse.error ? (
              <div className="text-red-600">{apiResponse.error}</div>
            ) : apiResponse.info ? (
              <div>{apiResponse.info}</div>
            ) : null}
            <button
              className="w-full bg-[#5035f6] text-white py-2 rounded hover:bg-[#3d28b1] cursor-pointer mt-4"
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