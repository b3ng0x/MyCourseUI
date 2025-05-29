import React, { useEffect, useState } from "react";
import Sidebar from "./components/Sidebar/Sidebar";
import VideoPlayer from "./components/VideoPlayer/VideoPlayer";
import "./App.css";

function App() {
  const [courses, setCourses] = useState([]);
  const [selectedLesson, setSelectedLesson] = useState(null);

  useEffect(() => {
    fetch("/courses-structured.json")
      .then((res) => res.json())
      .then((data) => {
        setCourses(data);

        // Auto-scroll to last watched lesson if exists
        const last = localStorage.getItem("lastWatched");
        if (last) {
          try {
            const parsed = JSON.parse(last);
            setSelectedLesson(parsed);
            setTimeout(() => {
              const el = document.querySelector(`[data-path='${parsed.path}']`);
              el?.scrollIntoView({ behavior: "smooth", block: "center" });
            }, 500);
          } catch (e) {}
        }
      });
  }, []);

  const markAsWatched = (lesson) => {
    const watched = JSON.parse(localStorage.getItem("watchedLessons") || "{}");
    watched[lesson.path] = true;
    localStorage.setItem("watchedLessons", JSON.stringify(watched));
    localStorage.setItem("lastWatched", JSON.stringify(lesson));
  };

  const unmarkAll = () => {
    localStorage.removeItem("watchedLessons");
    localStorage.removeItem("lastWatched");
    window.location.reload();
  };

  return (
    <div className="app">
      <Sidebar
        courses={courses}
        onSelect={setSelectedLesson}
        selected={selectedLesson}
        onResetProgress={unmarkAll}
      />
      <VideoPlayer
        lesson={selectedLesson}
        onWatch={markAsWatched}
      />
    </div>
  );
}

export default App;