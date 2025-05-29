import React from "react";
import "./Sidebar.css";

const Sidebar = ({ courses, onSelect, selected, onResetProgress }) => {
  const watched = JSON.parse(localStorage.getItem("watchedLessons") || "{}");

  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h1>Courses</h1>
        <button onClick={onResetProgress}>🗑 Reset Progress</button>
      </div>
      {courses.map((course) => (
        <div key={course.slug} className="course-block">
          <h2>{course.title}</h2>
          {course.chapters.map((chapter) => (
            <div key={chapter.title} className="chapter">
              <h3>{chapter.title}</h3>
              <ul>
                {chapter.lessons.map((lesson) => (
                  <li
                    key={lesson.path}
                    data-path={lesson.path}
                    className={
                      selected?.path === lesson.path ? "active" : ""
                    }
                    onClick={() => onSelect(lesson)}
                  >
                    <span>
                      {watched[lesson.path] ? "✅" : "⬜"} {lesson.title}
                    </span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default Sidebar;