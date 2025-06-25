import React from "react";
import { CheckCircle, ChevronLeft } from "lucide-react";

export const Navbar = () => {
  return (
    <div className="w-full bg-white border-b border-gray-200 shadow-sm flex items-center justify-between px-4 py-4">
      {/* Left Logo */}
      <div className="flex items-center gap-2">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg"
          alt="Logo"
          className="h-6 w-auto"
        />
      </div>

      {/* Progress Bar */}
      <div className="flex-1 mx-4 max-w-md">
        <div className="text-sm text-blue-600 font-semibold">
          0% COMPLETED{" "}
          <span className="text-black font-normal ml-1">0/107 Steps</span>
        </div>
        <div className="w-full bg-gray-200 h-2 rounded mt-1">
          <div className="h-2 bg-blue-600 rounded w-[0%]" />
        </div>
      </div>

      {/* Navigation & Action */}
      <div className="flex items-center gap-4 text-blue-600 text-sm font-semibold whitespace-nowrap">
        <button className="flex items-center gap-1 px-4 py-1 rounded-full border border-transparent hover:border-blue-600 hover:shadow-md transition-all duration-200 cursor-pointer">
          <ChevronLeft className="w-4 h-4" />
          Previous Topic
        </button>

        <button className="flex items-center gap-1 px-4 py-1 rounded-full border border-transparent hover:border-blue-600 hover:shadow-md transition-all duration-200 cursor-pointer">
          Mark as complete
          <CheckCircle className="w-4 h-4" />
        </button>
      </div>

      {/* User Avatar */}
      <div className="ml-4 cursor-pointer">
        <div className="flex items-center text-sm text-gray-600">
          <span className="hidden sm:inline-block mr-2">
            Hello, User!
          </span>
          <div className="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center">
            <svg
              className="w-6 h-6 text-white"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                fillRule="evenodd"
                d="M10 10a4 4 0 100-8 4 4 0 000 8zm-6 8a6 6 0 1112 0H4z"
                clipRule="evenodd"
              />
            </svg>
          </div>
        </div>
      </div>
    </div>
  );
};
