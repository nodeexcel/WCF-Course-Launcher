import React, { useState, useEffect } from 'react';
import { courseForms } from '../data/courseForms';

export const ContentModal = ({ heading, onClose }) => {
  const isDefault = heading === 'Assistant';
  const formConfig = courseForms[heading] || [];
  const [formData, setFormData] = useState({});

  useEffect(() => {
    setFormData({});
  }, [heading]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
  };

  return (
    <div className="fixed bottom-16 right-6 z-50 w-[400px] h-[450px] bg-white rounded-xl shadow-2xl flex flex-col border border-gray-200">
      <div className="flex items-center justify-between px-4 py-3 border-b border-gray-100 bg-[#5035f6] rounded-t-xl">
        <h2 className="text-lg font-bold text-white">{isDefault ? 'Assistant' : heading}</h2>
        <button
          className="text-white hover:text-gray-200 text-2xl font-bold ml-2"
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
          <form onSubmit={handleSubmit}>
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
              <button type="submit" className="w-full bg-[#5035f6] text-white py-2 rounded hover:bg-[#3d28b1]">Submit</button>
            )}
          </form>
        )}
      </div>
    </div>
  );
}; 