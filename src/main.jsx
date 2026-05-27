import React, { useMemo, useState } from "react";
import { createRoot } from "react-dom/client";
import {
  Award,
  BookOpen,
  BriefcaseBusiness,
  CalendarDays,
  Camera,
  Cpu,
  Download,
  ExternalLink,
  Github,
  GraduationCap,
  Home,
  Linkedin,
  Mail,
  MapPin,
  Menu,
  Plus,
  Rocket,
  Send,
  Sparkles,
  X
} from "lucide-react";
import "./styles.css";

const navItems = [
  { id: "home", label: "Portfolio", icon: Home },
  { id: "pmvikas", label: "PM Vikas", icon: CalendarDays },
  { id: "resume", label: "Resume", icon: Download }
];

const skills = [
  "Embedded Systems",
  "IoT Prototyping",
  "Arduino",
  "Sensor Integration",
  "Communication Systems",
  "Circuit Design",
  "Python Basics",
  "Technical Documentation"
];

const projects = [
  {
    title: "IoT Environment Monitor",
    copy: "A sensor-driven prototype concept for collecting temperature, humidity, and device status data for practical dashboards."
  },
  {
    title: "Smart Connectivity Notes",
    copy: "Structured internship learning logs focused on microcontrollers, networking basics, and real-world IoT use cases."
  },
  {
    title: "PM Vikas Activity Tracker",
    copy: "A 35-slot digital progress board for recording daily activity, evidence images, and reflective notes."
  }
];

const achievements = [
  "Selected for IoT Assistant internship exposure at IIIT Kottayam.",
  "Building a disciplined PM Vikas learning record from May 20 to June 30, 2026.",
  "Focused on practical electronics, communication, and future-skills documentation."
];

const statusOptions = ["Planned", "In Progress", "Completed", "Reviewed"];

function makeActivityDates() {
  const dates = [];
  const cursor = new Date(2026, 4, 20);
  const end = new Date(2026, 5, 30);

  while (cursor <= end && dates.length < 35) {
    const day = cursor.getDay();
    if (day !== 0 && day !== 6) {
      dates.push(
        cursor.toLocaleDateString("en-US", {
          weekday: "short",
          month: "short",
          day: "numeric",
          year: "numeric"
        })
      );
    }
    cursor.setDate(cursor.getDate() + 1);
  }

  return dates;
}

function App() {
  const [activePage, setActivePage] = useState("home");
  const [menuOpen, setMenuOpen] = useState(false);
  const CurrentPage =
    activePage === "pmvikas" ? PMVikasPage : activePage === "resume" ? ResumePage : HomePage;

  return (
    <div className="app-shell">
      <header className="topbar">
        <button className="brand" onClick={() => setActivePage("home")} aria-label="Go to portfolio">
          <span className="brand-mark">MSJ</span>
          <span>
            <strong>Mahima Sara Jacob</strong>
            <small>ECE | IoT Assistant</small>
          </span>
        </button>

        <button className="menu-button" onClick={() => setMenuOpen(!menuOpen)} aria-label="Toggle navigation">
          {menuOpen ? <X size={20} /> : <Menu size={20} />}
        </button>

        <nav className={menuOpen ? "nav-links open" : "nav-links"}>
          {navItems.map((item) => {
            const Icon = item.icon;
            return (
              <button
                key={item.id}
                className={activePage === item.id ? "nav-link active" : "nav-link"}
                onClick={() => {
                  setActivePage(item.id);
                  setMenuOpen(false);
                  window.scrollTo({ top: 0, behavior: "smooth" });
                }}
              >
                <Icon size={17} />
                {item.label}
              </button>
            );
          })}
        </nav>
      </header>

      <CurrentPage />
    </div>
  );
}

function HomePage() {
  return (
    <main>
      <section className="hero-section">
        <div className="hero-copy">
          <span className="eyebrow"><Sparkles size={16} /> Electronics and Communication Engineering</span>
          <h1>Building connected systems with clarity, discipline, and purpose.</h1>
          <p>
            I am Mahima Sara Jacob, an ECE student at College of Engineering Kidangoor, Kottayam,
            currently gaining practical IoT exposure as an Assistant intern at IIIT Kottayam.
          </p>
          <div className="hero-actions">
            <a className="primary-action" href="mailto:mahimasj07@gmail.com"><Mail size={18} /> Contact Me</a>
            <a className="secondary-action" href="https://www.linkedin.com/in/mahimasj" target="_blank" rel="noreferrer">
              <Linkedin size={18} /> LinkedIn
            </a>
          </div>
        </div>
        <div className="hero-panel">
          <div className="orbital-card">
            <Cpu size={40} />
            <strong>IoT Assistant Intern</strong>
            <span>IIIT Kottayam</span>
          </div>
          <div className="metric-grid">
            <span><strong>35</strong> PM Vikas slots</span>
            <span><strong>8+</strong> technical skills</span>
            <span><strong>2026</strong> active portfolio</span>
          </div>
        </div>
      </section>

      <section className="content-band split">
        <div>
          <span className="section-kicker">About Me</span>
          <h2>Professional profile</h2>
          <p>
            I enjoy understanding how hardware, communication, and software come together to solve
            practical problems. My focus is to grow as a confident engineer with strong technical
            fundamentals, organized documentation habits, and an eye for useful technology.
          </p>
        </div>
        <div className="info-list">
          <Info icon={GraduationCap} title="Education" text="B.Tech Electronics and Communication Engineering, College of Engineering Kidangoor, Kottayam." />
          <Info icon={BriefcaseBusiness} title="Internship" text="IoT Assistant internship at IIIT Kottayam with exposure to connected devices and future-skills workflows." />
          <Info icon={MapPin} title="Location" text="Kottayam, Kerala, India." />
        </div>
      </section>

      <section className="content-band">
        <span className="section-kicker">Capabilities</span>
        <h2>Skills and technical strengths</h2>
        <div className="skill-grid">
          {skills.map((skill) => <span className="skill-pill" key={skill}>{skill}</span>)}
        </div>
      </section>

      <section className="content-band">
        <span className="section-kicker">Selected Work</span>
        <h2>Projects and focus areas</h2>
        <div className="card-grid">
          {projects.map((project) => (
            <article className="feature-card" key={project.title}>
              <Rocket size={24} />
              <h3>{project.title}</h3>
              <p>{project.copy}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="content-band">
        <span className="section-kicker">Achievements</span>
        <h2>Milestones</h2>
        <div className="achievement-list">
          {achievements.map((item) => (
            <div className="achievement" key={item}><Award size={20} /> {item}</div>
          ))}
        </div>
      </section>

      <ContactStrip />
    </main>
  );
}

function Info({ icon: Icon, title, text }) {
  return (
    <article className="info-card">
      <Icon size={22} />
      <div>
        <h3>{title}</h3>
        <p>{text}</p>
      </div>
    </article>
  );
}

function PMVikasPage() {
  const dates = useMemo(makeActivityDates, []);
  const [activities, setActivities] = useState(() =>
    dates.map((date, index) => ({
      id: index + 1,
      date,
      status: index === 0 ? "In Progress" : "Planned",
      notes: "",
      imageName: ""
    }))
  );

  function updateActivity(id, field, value) {
    setActivities((current) =>
      current.map((activity) => activity.id === id ? { ...activity, [field]: value } : activity)
    );
  }

  const completed = activities.filter((activity) => activity.status === "Completed").length;

  return (
    <main>
      <section className="pm-hero">
        <div>
          <span className="eyebrow"><BookOpen size={16} /> FutureSkills activity dashboard</span>
          <h1>PM Vikas learning tracker</h1>
          <p>
            PM Vikas FutureSkills supports structured skill-building through daily learning,
            documentation, practice, and evidence-based progress. This tracker keeps each working
            day visible from May 20 to June 30, 2026, excluding Saturdays and Sundays.
          </p>
          <a className="primary-action" href="https://www.pmvishwakarma.gov.in/" target="_blank" rel="noreferrer">
            <ExternalLink size={18} /> Open PM Vikas FutureSkills
          </a>
        </div>
        <div className="progress-card">
          <span>Progress</span>
          <strong>{completed}/35</strong>
          <div className="progress-track"><span style={{ width: `${(completed / 35) * 100}%` }} /></div>
        </div>
      </section>

      <section className="tracker-toolbar">
        <div>
          <h2>Daily activity slots</h2>
          <p>Each slot includes date, status, notes, and picture upload evidence.</p>
        </div>
        <span className="gold-badge">Weekdays only</span>
      </section>

      <section className="activity-grid">
        {activities.map((activity) => (
          <article className="activity-card" key={activity.id}>
            <div className="activity-head">
              <span>Day {String(activity.id).padStart(2, "0")}</span>
              <strong>{activity.date}</strong>
            </div>
            <label>
              Status
              <select value={activity.status} onChange={(event) => updateActivity(activity.id, "status", event.target.value)}>
                {statusOptions.map((status) => <option key={status}>{status}</option>)}
              </select>
            </label>
            <label>
              Notes
              <textarea
                value={activity.notes}
                placeholder="Write activity details, learning outcome, or reflection."
                onChange={(event) => updateActivity(activity.id, "notes", event.target.value)}
              />
            </label>
            <label className="upload-box">
              <Camera size={18} />
              <span>{activity.imageName || "Upload picture"}</span>
              <input
                type="file"
                accept="image/*"
                onChange={(event) => updateActivity(activity.id, "imageName", event.target.files?.[0]?.name || "")}
              />
            </label>
            <button className="add-button" onClick={() => updateActivity(activity.id, "status", "Completed")}>
              <Plus size={17} /> Add Activity
            </button>
          </article>
        ))}
      </section>
    </main>
  );
}

function ResumePage() {
  return (
    <main>
      <section className="resume-hero">
        <div>
          <span className="eyebrow"><Download size={16} /> Resume and contact</span>
          <h1>Let us build something meaningful.</h1>
          <p>
            I am available for academic collaboration, internship conversations, and learning-focused
            opportunities in electronics, communication, and IoT systems.
          </p>
          <div className="hero-actions">
            <a className="primary-action" href="/resume-mahima-sara-jacob.txt" download>
              <Download size={18} /> Download Resume
            </a>
            <a className="secondary-action" href="mailto:mahimasj07@gmail.com"><Send size={18} /> Email</a>
          </div>
        </div>
        <aside className="contact-card">
          <h2>Contact</h2>
          <a href="mailto:mahimasj07@gmail.com"><Mail size={18} /> mahimasj07@gmail.com</a>
          <a href="https://www.linkedin.com/in/mahimasj" target="_blank" rel="noreferrer"><Linkedin size={18} /> LinkedIn profile</a>
          <a href="https://github.com/mahimasj07/final-pm.git" target="_blank" rel="noreferrer"><Github size={18} /> GitHub repository</a>
        </aside>
      </section>

      <section className="content-band split">
        <div>
          <span className="section-kicker">Resume Snapshot</span>
          <h2>Mahima Sara Jacob</h2>
          <p>ECE student, College of Engineering Kidangoor, Kottayam. IoT Assistant intern at IIIT Kottayam.</p>
        </div>
        <div className="timeline">
          <div><strong>Education</strong><span>B.Tech ECE</span></div>
          <div><strong>Internship</strong><span>IoT Assistant, IIIT Kottayam</span></div>
          <div><strong>Focus</strong><span>IoT, embedded systems, documentation</span></div>
        </div>
      </section>
    </main>
  );
}

function ContactStrip() {
  return (
    <section className="contact-strip">
      <div>
        <span className="section-kicker">Contact</span>
        <h2>Open to learning, collaboration, and technical growth.</h2>
      </div>
      <div className="contact-actions">
        <a href="mailto:mahimasj07@gmail.com"><Mail size={18} /> Email</a>
        <a href="https://www.linkedin.com/in/mahimasj" target="_blank" rel="noreferrer"><Linkedin size={18} /> LinkedIn</a>
      </div>
    </section>
  );
}

createRoot(document.getElementById("root")).render(<App />);
