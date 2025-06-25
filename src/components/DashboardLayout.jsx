import React, { useState } from 'react';
import { Navbar } from './navbar';
import { Sidebar } from './sidebar';
import { ContentArea } from './ContentArea';
import { useLocation } from 'react-router-dom';
import { ContentModal } from './ContentModal';

const DashboardLayout = () => {
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const selectedTitle = params.get('title') || '';
  const [modalOpen, setModalOpen] = useState(false);

  return (
    <div className='flex flex-col h-screen'>
      <Navbar />
      <div className='flex flex-1'>
        <Sidebar />
        <div className='flex-1'>
          <ContentArea selectedTitle={selectedTitle} />
        </div>
      </div>
      {modalOpen && (
        <div className="fixed bottom-20 right-6 z-50">
          <ContentModal heading={selectedTitle || 'Assistant'} onClose={() => setModalOpen(false)} />
        </div>
      )}
      <button
        className="fixed bottom-6 right-6 z-50 bg-[#5035f6] border-2 border-white text-white rounded-full w-14 h-14 flex items-center justify-center shadow-lg hover:bg-[#3d28b1] focus:outline-none"
        onClick={() => setModalOpen(true)}
        title="Open Chat/Modal"
        style={{ boxShadow: '0 4px 24px 0 rgba(80,53,246,0.15)' }}
      >
        <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="16" cy="16" r="16" fill="#5035f6" />
          <path d="M10 16C10 13.2386 12.6863 11 16 11C19.3137 11 22 13.2386 22 16C22 18.7614 19.3137 21 16 21C15.3812 21 14.7852 20.9172 14.2222 20.7642C13.9642 20.6952 13.6952 20.6952 13.4372 20.7642L12.2222 21.0691C11.7852 21.1792 11.4208 20.8148 11.5309 20.3778L11.8358 19.1628C11.9048 18.9048 11.9048 18.6358 11.8358 18.3778C11.0828 17.8148 10.5 16.9614 10.5 16Z" stroke="white" strokeWidth="2"/>
          <circle cx="13.5" cy="16" r="1" fill="white" />
          <circle cx="16" cy="16" r="1" fill="white" />
          <circle cx="18.5" cy="16" r="1" fill="white" />
        </svg>
      </button>
    </div>
  );
};

export default DashboardLayout; 