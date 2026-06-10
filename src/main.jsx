import React, { useMemo, useState, useEffect } from "react";
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
  Search,
  SlidersHorizontal,
  X
} from "lucide-react";
import "./styles.css";

const navItems = [
  { id: "home", label: "Portfolio", icon: Home },
  { id: "pmvikas", label: "PM Vikas", icon: CalendarDays },
  { id: "tinkercad", label: "Tinkercad Projects", icon: Rocket },
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

function normalizeProjectName(text) {
  return text
    .replace(/_/g, " ")
    .replace(/\s+/g, " ")
    .replace(/\s*\(\s*/g, " (")
    .replace(/\s*\)\s*/g, ")")
    .trim()
    .toLowerCase()
    .replace(/(^|[\s-])[a-z]/g, (match) => match.toUpperCase());
}

function classifyProjectType(text) {
  const key = text.toLowerCase();
  if (
    key.includes("actuator") ||
    key.includes("motor") ||
    key.includes("servo") ||
    key.includes("display") ||
    key.includes("led") ||
    key.includes("piezo") ||
    key.includes("neopixel") ||
    key.includes("buffer") ||
    key.includes("segment")
  ) {
    return "Actuator";
  }

  if (
    key.includes("sensor") ||
    key.includes("photoresistor") ||
    key.includes("potentiometer") ||
    key.includes("temperature") ||
    key.includes("tilt") ||
    key.includes("ultrasonic") ||
    key.includes("force") ||
    key.includes("gas") ||
    key.includes("ambient") ||
    key.includes("pir")
  ) {
    return "Sensor";
  }

  return "Project";
}

function generateProjectDescription(text) {
  const cleaned = normalizeProjectName(text).replace(/\s*\(.*?\)/g, "").trim();
  const type = classifyProjectType(text);
  return `${type} experiment for ${cleaned}. Arduino, Tinkercad, and IoT systems with project wiring and code summaries.`;
}

function chooseProjectIcon(text) {
  const key = text.toLowerCase();
  if (key.includes("motor") || key.includes("servo") || key.includes("actuator") || key.includes("display") || key.includes("neopixel") || key.includes("led") || key.includes("piezo") || key.includes("buffer") || key.includes("segment")) {
    return Rocket;
  }
  if (key.includes("sensor") || key.includes("photoresistor") || key.includes("potentiometer") || key.includes("temperature") || key.includes("tilt") || key.includes("ultrasonic") || key.includes("force") || key.includes("gas") || key.includes("ambient") || key.includes("pir")) {
    return Cpu;
  }
  return Sparkles;
}

function App() {
  const [activePage, setActivePage] = useState("home");
  const [menuOpen, setMenuOpen] = useState(false);
  const CurrentPage =
    activePage === "pmvikas"
      ? PMVikasPage
      : activePage === "tinkercad"
      ? TinkercadPage
      : activePage === "resume"
      ? ResumePage
      : HomePage;

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

function TinkercadPage() {
  const [projectsData, setProjectsData] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [statusFilter, setStatusFilter] = useState("all");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    setLoading(true);
    fetch("https://api.github.com/repos/mahimasj07/sensors-and-actuators/git/trees/main?recursive=1")
      .then((response) => {
        if (!response.ok) throw new Error("GitHub API error");
        return response.json();
      })
      .then((data) => {
        const folders = Array.from(
          new Set(
            data.tree
              .filter((item) => item.type === "tree")
              .map((item) => item.path.split("/")[0])
              .filter(Boolean)
          )
        ).sort((a, b) => a.localeCompare(b, "en", { sensitivity: "base" }));

        setProjectsData(
          folders.map((folder) => {
            const projectName = normalizeProjectName(folder);
            const projectType = classifyProjectType(folder);
            return {
              id: folder,
              folder,
              title: projectName,
              projectType,
              description: generateProjectDescription(folder),
              githubUrl: `https://github.com/mahimasj07/sensors-and-actuators/tree/main/${encodeURIComponent(folder)}`,
              Icon: chooseProjectIcon(folder)
            };
          })
        );
        setError("");
      })
      .catch(() => {
        setError("Unable to load sensor and actuator projects from GitHub. Please refresh to retry.");
      })
      .finally(() => setLoading(false));
  }, []);

  const filteredProjects = projectsData.filter((project) => {
    const query = searchQuery.trim().toLowerCase();
    const matchesSearch =
      !query ||
      project.title.toLowerCase().includes(query) ||
      project.description.toLowerCase().includes(query) ||
      project.projectType.toLowerCase().includes(query);
    const matchesFilter =
      statusFilter === "all" ||
      (statusFilter === "sensors" && project.projectType === "Sensor") ||
      (statusFilter === "actuators" && project.projectType === "Actuator");
    return matchesSearch && matchesFilter;
  });

  const totalProjects = projectsData.length;
  const totalSensors = projectsData.filter((project) => project.projectType === "Sensor").length;
  const totalActuators = projectsData.filter((project) => project.projectType === "Actuator").length;

  return (
    <main>
      <section className="hero-section hero-tinkercad">
        <div className="hero-copy">
          <span className="eyebrow"><Sparkles size={16} /> Arduino • Tinkercad • IoT Systems</span>
          <h1>Tinkercad Projects</h1>
          <p className="hero-tagline">Sensors & Actuators Laboratory</p>
          <p className="hero-description">PM Vikas Internship Project</p>
          <p>
            Explore every sensor and actuator experiment from the repository with a premium laboratory dashboard experience.
          </p>
          <div className="hero-actions">
            <a className="primary-action" href="https://github.com/mahimasj07/sensors-and-actuators" target="_blank" rel="noreferrer">
              <ExternalLink size={18} /> View Full Repository
            </a>
          </div>
        </div>

        <div className="hero-panel stats-panel">
          <div className="stat-card">
            <strong>{totalProjects}</strong>
            <span>Total Projects</span>
          </div>
          <div className="stat-card">
            <strong>{totalSensors}</strong>
            <span>Total Sensors</span>
          </div>
          <div className="stat-card">
            <strong>{totalActuators}</strong>
            <span>Total Actuators</span>
          </div>
        </div>
      </section>

      <section className="content-band">
        <div className="tinkercad-toolbar">
          <div className="search-panel">
            <label className="search-field">
              <Search size={18} />
              <input
                type="search"
                value={searchQuery}
                onChange={(event) => setSearchQuery(event.target.value)}
                placeholder="Search Tinkercad projects"
                aria-label="Search Tinkercad projects"
              />
            </label>
            <div className="filter-group">
              <button
                className={statusFilter === "all" ? "filter-pill active" : "filter-pill"}
                onClick={() => setStatusFilter("all")}
              >
                All Projects
              </button>
              <button
                className={statusFilter === "sensors" ? "filter-pill active" : "filter-pill"}
                onClick={() => setStatusFilter("sensors")}
              >
                Sensors
              </button>
              <button
                className={statusFilter === "actuators" ? "filter-pill active" : "filter-pill"}
                onClick={() => setStatusFilter("actuators")}
              >
                Actuators
              </button>
            </div>
          </div>

          <div className="filter-summary">
            <SlidersHorizontal size={18} />
            <span>{filteredProjects.length} visible projects</span>
          </div>
        </div>

        {error ? <div className="alert-band">{error}</div> : null}

        {loading ? (
          <div className="loading-panel">Loading Tinkercad projects...</div>
        ) : (
          <div className="project-grid">
            {filteredProjects.length > 0 ? (
              filteredProjects.map((project) => {
                const Icon = project.Icon;
                return (
                  <article className="project-card" key={project.id}>
                    <div className="project-card-head">
                      <div className="project-icon">
                        <Icon size={22} />
                      </div>
                      <div>
                        <span className="project-type">{project.projectType}</span>
                        <h3>{project.title}</h3>
                      </div>
                    </div>
                    <p>{project.description}</p>
                    <a className="secondary-action card-link" href={project.githubUrl} target="_blank" rel="noreferrer">
                      <Github size={16} /> View on GitHub
                    </a>
                  </article>
                );
              })
            ) : (
              <div className="empty-state">No projects match the current search and filter.</div>
            )}
          </div>
        )}
      </section>

      <section className="content-band" style={{ paddingTop: "0" }}>
        <div className="project-note">
          <h2>How it works</h2>
          <p>
            This page discovers folders from your sensors-and-actuators GitHub repository in real time. Each lab appears as a card with an auto-generated summary, type badge, and direct repository link.
          </p>
        </div>
      </section>
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
      current.map((activity) => (activity.id === id ? { ...activity, [field]: value } : activity))
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
