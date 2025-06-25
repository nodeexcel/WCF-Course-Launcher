import React from 'react';

export const ContentArea = ({ selectedTitle }) => {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold text-blue-700">{selectedTitle}</h1>
      <p className="mt-4 text-gray-600">
        This is the content area for <strong>{selectedTitle}</strong>.
      </p>
    </div>
  );
};
