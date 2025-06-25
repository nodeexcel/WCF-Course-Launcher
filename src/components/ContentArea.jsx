import React from 'react';

export const ContentArea = ({ selectedTitle }) => {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold text-blue-700">{selectedTitle}</h1>
    </div>
  );
};
