import React from 'react';

const TimeInterval = ({ onIntervalSelect }) => {
  return (
    <div className="time-interval">
      <div className="btn-group">
        <button onClick={() => onIntervalSelect('current')} className="btn btn-primary">Now</button>
        <button onClick={() => onIntervalSelect('forecast')} className="btn btn-primary">Next 5 Days</button>
      </div>
    </div>
  );
};

export default TimeInterval;
