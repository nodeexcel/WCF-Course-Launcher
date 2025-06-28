import React, { useState } from "react";
import { ChevronLeft, ChevronDown, ChevronUp } from "lucide-react";
import { useNavigate, useLocation } from 'react-router-dom';

 const sidebarData = [
  {
    id: 1,
    title: "I. Strong Foundations Scheme",
    count: 5,
    children: [
      "Choosing a Niche",
      "Market Research",
      "Target Group",
      "The Topic of the Course and the Problem you are solving",
      "4 Ways to Generate an Online Course Idea",
    ],
  },
  {
    id: 2,
    title: "II. Course Creation Accelerator",
    count: 6,
    children: [
      "Live Product iDEAS",
      "Evergreen",
      "Product Ladder",
      "Course Structure",
      "Subscription Product",
      "Packaging Process"
    ],
  },
  {
    id: 3,
    title: "III. Expert Positioning Formula",
    count: 4,
    children: [
      "Expert Avatar - Life Story",
      "3 expert actions - articles",
      "3 expert activities - articles, offline appearances, interviews",
      "Creating content a month in advance"
      
    ],
  },
  {
    id:4,
    title: "IV. Magnetic Marketing System",
    count: 5,
    children: [
      "Ideas for content rolls",
      "Script for the content roll",
      "Content for lead magnet page",
      "Text ABOUT YOU on the landing page",
      "Mini offer - product ideas + headline and benefits"
    ]
  }
];


export const Sidebar = ({ nicheCompleted }) => {
  const [isOpen, setIsOpen] = useState(true);
  const [expandedItem, setExpandedItem] = useState(null);
  const navigate = useNavigate();
  const location = useLocation();
  const params = new URLSearchParams(location.search);
  const selectedTitle = params.get('title') || '';

  const toggleSidebar = () => setIsOpen((prev) => !prev);
  const toggleExpand = (id) =>
    setExpandedItem((prev) => (prev === id ? null : id));

  // Title click handler
  const handleTitleClick = (title) => {
    navigate(`/dashboard?title=${encodeURIComponent(title)}`);
  };

  return (
    <div className="flex">
      {/* Sidebar */}
      <div
        className={`transition-all duration-300 bg-white border-r border-gray-200 overflow-hidden relative ${isOpen ? 'w-80' : 'w-10'}`}
        style={{ minWidth: isOpen ? undefined : 40 }}
      >
        <div
          className={`absolute z-10 left-0 right-0 ${isOpen ? 'top-2 right-2 flex justify-end' : 'top-0 flex justify-center'}`}
          style={{ right: isOpen ? 8 : 0 }}
        >
          {!isOpen && (
            <div className="w-full bg-[#5035f6] flex justify-center items-center" style={{ height: 36, borderBottomLeftRadius: 8, borderBottomRightRadius: 8 }}>
              <button
                onClick={toggleSidebar}
                className="flex items-center justify-center cursor-pointer"
                style={{ width: 32, height: 32 }}
                title="Expand sidebar"
              >
                <ChevronLeft className="w-6 h-6 rotate-180 text-white" />
              </button>
            </div>
          )}
          {isOpen && (
            <button
              onClick={toggleSidebar}
              className="w-8 h-8 border border-[#5035f6] bg-white rounded-full flex items-center justify-center cursor-pointer shadow"
              style={{ width: 32, height: 32 }}
              title="Collapse sidebar"
            >
              <ChevronLeft className="w-4 h-4 text-[#5035f6]" />
            </button>
          )}
        </div>
        {isOpen ? (
          <>
            <div className="bg-[#5035f6] text-white px-4 py-3 flex justify-between items-center relative">
              <h2 className="text-[15px] font-semibold flex items-center gap-2">
                📘 WOW Courses Formula 3.0
              </h2>
            </div>
            {/* List of Topics */}
            <div className="divide-y">
              {sidebarData.map((item) => (
                <div key={item.id} className="p-4">
                  <div className="flex items-start gap-2">
                    <input type="radio" name="topics" className="mt-1" onClick={() => handleTitleClick(item.title)} checked={selectedTitle === item.title} readOnly />
                    <div>
                      <h3
                        className={`text-blue-700 text-sm cursor-pointer ${selectedTitle === item.title ? 'font-bold text-blue-900' : 'font-semibold'}`}
                        onClick={() => handleTitleClick(item.title)}
                      >
                        {item.title}
                      </h3>
                      <button
                        className={`mt-2 px-4 py-1 flex items-center gap-2 rounded-full text-sm font-semibold transition-all duration-200 cursor-pointer ${
                          expandedItem === item.id
                            ? "border border-blue-600 text-blue-700"
                            : "text-blue-700"
                        }`}
                        onClick={() => toggleExpand(item.id)}
                      >
                        {expandedItem === item.id ? (
                          <ChevronUp className="w-4 h-4" />
                        ) : (
                          <ChevronDown className="w-4 h-4" />
                        )}
                        {item.count} Topics
                      </button>

                      {/* Children list */}
                      {expandedItem === item.id && (
                        <ul className="mt-4 space-y-2 bg-gray-50 p-4 rounded">
                          {item.children.map((child, index) => {
                            const isChoosingNiche = child === 'Choosing a Niche';
                            const isDisabled = !isChoosingNiche && !nicheCompleted;
                            return (
                              <li
                                key={index}
                                className={`flex items-center gap-2 cursor-pointer ${selectedTitle === child ? 'font-bold text-blue-900' : ''} ${isDisabled ? 'opacity-50 cursor-not-allowed' : ''}`}
                                onClick={() => {
                                  if (!isDisabled) handleTitleClick(child);
                                }}
                                style={isDisabled ? { pointerEvents: 'none' } : {}}
                              >
                                <input type="radio" name="subtopic" checked={selectedTitle === child} readOnly disabled={isDisabled} />
                                <span className="text-sm text-gray-800  truncate max-w-[180px]">{child}</span>
                              </li>
                            );
                          })}
                        </ul>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </>
        ) : null}
      </div>
    </div>
  );
};
