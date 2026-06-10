from pathlib import Path

main = '''import React, { useEffect, useMemo, useRef, useState } from "react";
import { createRoot } from "react-dom/client";
import { motion } from "framer-motion";
import {
  Award,
  BookOpen,
  BriefcaseBusiness,
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
  Search,
  SlidersHorizontal,
  Sparkles,
  X
} from "lucide-react";
import "./styles.css";

const navItems = [
  { id: "home", label: "Home", icon: Home },
  { id: "about", label: "About", icon: BookOpen },
  { id: "skills", label: "Skills", icon: Sparkles },
  { id: "projects", label: "Projects", icon: Rocket },
  { id: "tinkercad", label: "Tinkercad Projects", icon: Cpu },
  { id: "contact", label: "Contact", icon: Mail }
];

const skillGroups = [
  {
    title: "Programming",
    items: ["C/C++", "Python", "JavaScript", "MATLAB"],
    level: 92
  },
  {
    title: "IoT",
    items: ["Sensor fusion", "MQTT", "Data logging", "Cloud-ready"],
    level: 88
  },
  {
    title: "Arduino",
    items: ["Uno", "Nano", "Mega", "Tinkercad prototypes"],
    level: 94
  },
  {
    title: "Embedded Systems",
    items: ["Microcontrollers", "Peripheral design", "Low-power mode"],
    level: 89
  },
  {
    title: "Electronics",
    items: ["Analog design", "PCB flow", "Circuit debugging"],
    level: 85
  },
  {
    title: "Communication",
    items: ["SPI", "I2C", "UART", "Wireless protocols"],
    level: 86
  },
  {
    title: "Web & UX",
    items: ["React", "Modern UI", "Responsive design"],
    level: 80
  }
];

const featuredProjects = [
  {
    title: "Ambient Lab Monitor",
    description:
      "A sensor-driven project combining temperature, light, and sound monitoring into a responsive dashboard experience.",
    tags: ["Arduino", "Sensors", "IoT"],
    github: "https://github.com/mahimasj07/neon-mermaid"
  },
  {
    title: "Actuator Control Panel",
    description:
      "A premium interface for actuator experiments, including motors, LEDs, and servo actuators with modern interaction.",
    tags: ["Actuators", "Embedded", "UI"],
    github: "https://github.com/mahimasj07/sensors-and-actuators"
  },
  {
    title: "Smart Street Light Prototype",
    description:
      "A Tinkercad-based automation system that blends sensor input and actuator response for efficient lighting control.",
    tags: ["Tinkercad", "Automation", "Prototype"],
    github: "https://github.com/mahimasj07/sensors-and-actuators"
  }
];

const overviewItems = [
  {
    name: "Academic background",
    detail: "B.Tech in Electronics & Communication Engineering from College of Engineering Kidangoor."
  },
  {
    name: "Engineering interests",
    detail: "Embedded devices, intelligent sensor systems, and polished prototype experiences."
  },
  {
    name: "Internship experience",
    detail: "IoT Assistant internship at IIIT Kottayam with hands-on work in communication systems."
  },
  {
    name: "Passions",
    detail: "Intuitive hardware-software integration, glowing interface design, and structured documentation."
  }
];

const timelineEvents = [
  {
    year: "2023",
    title: "B.Tech admission",
    description: "Started ECE studies with strong fundamentals in circuits, communication, and embedded logic."
  },
  {
    year: "2025",
    title: "IoT Assistant internship",
    description: "Joined IIIT Kottayam to prototype systems, document learning, and support sensor-actuator labs."
  },
  {
    year: "2026",
    title: "Tinkercad portfolio",
    description: "Building a premium lab portfolio focused on sensors & actuators for recruiters and mentors."
  }
];

const sectionIds = ["home", "about", "skills", "projects", "tinkercad", "contact"];

function normalizeProjectName(text) {
  return text
    .replace(/_/g, " ")
    .replace(/\s+/g, " ")
    .replace(/\s*\(\s*/g, " (")
    .replace(/\s*\)\s*/g, ")")
    .trim()
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
    key.includes("neopixel") ||
    key.includes("piezo") ||
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
  return `${type} experiment centered on ${cleaned} with Arduino-driven design and documentation.`;
}

function chooseProjectIcon(text) {
  const key = text.toLowerCase();
  if (
    key.includes("motor") ||
    key.includes("servo") ||
    key.includes("actuator") ||
    key.includes("display") ||
    key.includes("neopixel") ||
    key.includes("led") ||
    key.includes("piezo") ||
    key.includes("buffer") ||
    key.includes("segment")
  ) {
    return Rocket;
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
    return Cpu;
  }
  return Sparkles;
}

function App() {
  const [activeSection, setActiveSection] = useState("home");
  const [showMobileMenu, setShowMobileMenu] = useState(false);
  const [tinkercadProjects, setTinkercadProjects] = useState([]);
  const [tinkercadLoading, setTinkercadLoading] = useState(false);
  const [tinkercadError, setTinkercadError] = useState("");
  const [searchQuery, setSearchQuery] = useState("");
  const [statusFilter, setStatusFilter] = useState("all");

  const sectionsRef = useRef({});

  useEffect(() => {
    const handleScroll = () => {
      const offset = window.scrollY + 180;
      let active = "home";
      sectionIds.forEach((id) => {
        const section = sectionsRef.current[id];
        if (!section) return;
        if (section.offsetTop <= offset) {
          active = id;
        }
      });
      setActiveSection(active);
    };

    handleScroll();
    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  useEffect(() => {
    setTinkercadLoading(true);
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

        setTinkercadProjects(
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
        setTinkercadError("");
      })
      .catch(() => {
        setTinkercadError("Unable to load Tinkercad projects right now. Please refresh to retry.");
      })
      .finally(() => setTinkercadLoading(false));
  }, []);

  const filteredTinkercad = useMemo(() => {
    const query = searchQuery.trim().toLowerCase();
    return tinkercadProjects.filter((project) => {
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
  }, [searchQuery, statusFilter, tinkercadProjects]);

  const totalProjects = tinkercadProjects.length;
  const totalSensors = tinkercadProjects.filter((project) => project.projectType === "Sensor").length;
  const totalActuators = tinkercadProjects.filter((project) => project.projectType === "Actuator").length;

  const scrollToSection = (id) => {
    setShowMobileMenu(false);
    const section = sectionsRef.current[id];
    section?.scrollIntoView({ behavior: "smooth", block: "start" });
  };

  return (
    <div className="relative min-h-screen overflow-x-hidden bg-[#050505] text-white">
      <div className="pointer-events-none absolute inset-0 overflow-hidden">
        <span className="orb top-[6%] left-6 h-48 w-48 bg-violet/30 blur-3xl" />
        <span className="orb top-1/3 right-16 h-36 w-36 bg-gold/20 blur-3xl" />
        <span className="orb bottom-10 left-20 h-28 w-28 bg-violetSoft/30 blur-3xl" />
        <span className="particle top-24 left-[35%]" />
        <span className="particle top-[18%] right-24" />
        <span className="particle bottom-28 right-[22%]" />
      </div>

      <header className="glass-panel fixed inset-x-0 top-4 z-50 mx-auto flex w-[calc(100%-2rem)] max-w-7xl items-center justify-between gap-4 rounded-[32px] border-violet/30 bg-white/5 px-5 py-4 shadow-glow backdrop-blur-3xl transition-all duration-500 sm:px-8">
        <button
          className="flex items-center gap-3 text-left"
          onClick={() => scrollToSection("home")}
          aria-label="Go to home"
        >
          <span className="grid h-12 w-12 place-items-center rounded-2xl bg-gradient-to-br from-violet via-violetSoft to-gold text-black shadow-gold">
            MSJ
          </span>
          <span className="space-y-1 text-sm text-slate-200">
            <span className="block font-semibold text-white">Mahima Sara Jacob</span>
            <span className="text-xs text-slate-400">ECE | IoT & Embedded Systems</span>
          </span>
        </button>

        <nav className="hidden items-center gap-2 xl:flex">
          {navItems.map((item) => {
            const Icon = item.icon;
            return (
              <button
                key={item.id}
                onClick={() => scrollToSection(item.id)}
                className={`group inline-flex items-center gap-2 rounded-full px-5 py-3 text-sm font-medium transition duration-300 ${
                  activeSection === item.id
                    ? "bg-white/10 text-white ring-1 ring-white/20"
                    : "text-slate-300 hover:bg-white/10 hover:text-white"
                }`}
              >
                <Icon size={16} />
                <span>{item.label}</span>
              </button>
            );
          })}
        </nav>

        <button
          className="inline-flex h-12 w-12 items-center justify-center rounded-2xl border border-white/10 bg-white/5 text-white xl:hidden"
          onClick={() => setShowMobileMenu((state) => !state)}
          aria-label="Toggle navigation"
        >
          {showMobileMenu ? <X size={20} /> : <Menu size={20} />}
        </button>
      </header>

      {showMobileMenu ? (
        <div className="glass-panel fixed inset-x-4 top-20 z-40 rounded-[28px] border-white/10 bg-black/70 px-4 py-5 shadow-glow backdrop-blur-3xl xl:hidden">
          <div className="space-y-3">
            {navItems.map((item) => (
              <button
                key={item.id}
                onClick={() => scrollToSection(item.id)}
                className="flex w-full items-center gap-3 rounded-2xl border border-white/10 bg-white/5 px-4 py-3 text-left text-sm text-slate-200 transition hover:bg-white/10 hover:text-white"
              >
                <item.icon size={16} />
                {item.label}
              </button>
            ))}
          </div>
        </div>
      ) : null}

      <main className="relative mx-auto max-w-7xl px-4 pb-24 pt-32 sm:px-6 lg:px-8">
        <section
          id="home"
          ref={(el) => (sectionsRef.current.home = el)}
          className="relative overflow-hidden rounded-[40px] border border-white/10 bg-[#09060f]/80 p-8 shadow-glow backdrop-blur-3xl sm:p-12 lg:p-16"
        >
          <motion.div
            initial={{ opacity: 0, y: 24 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.85, ease: "easeOut" }}
            className="grid gap-10 lg:grid-cols-[1.15fr_0.85fr] lg:items-center"
          >
            <div className="space-y-8">
              <span className="inline-flex items-center gap-3 rounded-full border border-violet/30 bg-violet/10 px-4 py-2 text-xs uppercase tracking-[0.28em] text-violetSoft shadow-glow">
                <Sparkles size={16} /> Premium Engineering Portfolio
              </span>
              <div className="space-y-4">
                <p className="text-sm uppercase tracking-[0.36em] text-violetSoft/90">MAHIMA SARA JACOB</p>
                <h1 className="text-5xl font-semibold leading-tight tracking-[-0.06em] text-white sm:text-6xl lg:text-7xl">
                  Electronics & Communication Engineer
                </h1>
                <p className="max-w-3xl text-lg leading-8 text-slate-300 sm:text-xl">
                  IoT • Embedded Systems • Arduino • Sensors & Actuators — building luxurious lab interfaces and polished hardware prototypes for recruiters, mentors, and internship teams.
                </p>
              </div>

              <div className="flex flex-wrap gap-4">
                <a href="#projects" className="button-primary">
                  View Projects
                </a>
                <a href="#contact" className="button-secondary">
                  Contact Me
                </a>
                <a href="#" className="button-secondary">
                  <Download size={16} /> Download Resume
                </a>
              </div>

              <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
                {[
                  "High-end IoT concept design",
                  "Sensor-actuator labs",
                  "Modern embedded UX"
                ].map((text) => (
                  <div key={text} className="glass-panel flex items-center gap-3 border-violet/20 p-4">
                    <span className="grid h-12 w-12 place-items-center rounded-2xl bg-violet/15 text-violetSoft">
                      <Sparkles size={20} />
                    </span>
                    <p className="text-sm text-slate-200">{text}</p>
                  </div>
                ))}
              </div>
            </div>

            <div className="relative rounded-[36px] border border-white/10 bg-[#0f0b1b]/90 p-8 shadow-glow backdrop-blur-3xl">
              <div className="absolute -right-14 top-4 h-28 w-28 rounded-full bg-violetSoft/20 blur-3xl" />
              <div className="absolute left-10 top-24 h-20 w-20 rounded-full bg-gold/20 blur-3xl" />
              <div className="relative z-10 grid gap-6">
                <div className="space-y-3 rounded-[28px] border border-white/10 bg-white/5 p-6">
                  <p className="text-sm uppercase tracking-[0.28em] text-violetSoft">Lab essence</p>
                  <h2 className="mt-4 text-3xl font-semibold text-white">Future-ready systems</h2>
                  <p className="text-slate-300">A refined portfolio built for engineering recruiters, internship coordinators, and research mentors.</p>
                </div>
                <div className="grid gap-4 sm:grid-cols-2">
                  <div className="glass-panel rounded-[28px] border-violet/20 p-5">
                    <p className="text-sm uppercase tracking-[0.28em] text-violetSoft">Experience</p>
                    <p className="mt-3 text-4xl font-semibold text-white">IoT Assistant</p>
                  </div>
                  <div className="glass-panel rounded-[28px] border-gold/20 p-5">
                    <p className="text-sm uppercase tracking-[0.28em] text-violetSoft">Focus</p>
                    <p className="mt-3 text-4xl font-semibold text-white">Sensors & Actuators</p>
                  </div>
                </div>
              </div>
            </div>
          </motion.div>
        </section>

        <section id="about" ref={(el) => (sectionsRef.current.about = el)} className="mt-24 space-y-10">
          <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
            <div>
              <p className="section-subtitle">About</p>
              <h2 className="section-heading">Engineering fundamentals with premium polish</h2>
            </div>
            <div className="rounded-full border border-violet/20 bg-white/5 px-4 py-2 text-sm text-slate-300">
              Academic excellence, technical craftsmanship, and future skills.
            </div>
          </div>

          <div className="grid gap-6 xl:grid-cols-[0.95fr_1.05fr]">
            <motion.div
              initial={{ opacity: 0, y: 32 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.2 }}
              className="glass-panel border-violet/20 p-8"
            >
              <p className="text-sm uppercase tracking-[0.28em] text-violetSoft">Professional story</p>
              <h3 className="mt-4 text-3xl font-semibold text-white">A focused engineering pathway</h3>
              <p className="mt-4 text-slate-300 leading-8">
                As an ECE student and IoT enthusiast, I create systems where hardware, firmware, and interface design work together. My portfolio is built to highlight strong technical foundations, polished prototypes, and clear engineering communication.
              </p>
              <div className="mt-8 space-y-4">
                {overviewItems.map((item) => (
                  <div key={item.name} className="rounded-3xl border border-white/10 bg-white/5 p-5">
                    <p className="text-sm uppercase tracking-[0.22em] text-violetSoft">{item.name}</p>
                    <p className="mt-2 text-base leading-7 text-slate-300">{item.detail}</p>
                  </div>
                ))}
              </div>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 32 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.2 }}
              className="space-y-6"
            >
              <div className="flex items-center justify-between gap-4 rounded-[32px] border border-white/10 bg-[#111111]/80 p-6 shadow-glow">
                <div>
                  <p className="text-sm uppercase tracking-[0.28em] text-violetSoft">Timeline</p>
                  <h3 className="mt-3 text-2xl font-semibold text-white">High-end journey</h3>
                </div>
                <span className="rounded-full bg-gold/15 px-4 py-2 text-sm font-semibold text-gold">Recruiter-ready</span>
              </div>

              <div className="space-y-4">
                {timelineEvents.map((event) => (
                  <div key={event.year} className="glass-panel border-violet/20 p-6">
                    <div className="flex items-center justify-between gap-4">
                      <div>
                        <p className="text-xl font-semibold text-white">{event.title}</p>
                        <p className="mt-2 text-sm uppercase tracking-[0.24em] text-violetSoft">{event.year}</p>
                      </div>
                      <div className="rounded-full bg-white/10 px-4 py-2 text-sm text-slate-200">Milestone</div>
                    </div>
                    <p className="mt-4 text-slate-300 leading-7">{event.description}</p>
                  </div>
                ))}
              </div>
            </motion.div>
          </div>
        </section>

        <section id="skills" ref={(el) => (sectionsRef.current.skills = el)} className="mt-24">
          <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
            <div>
              <p className="section-subtitle">Skills</p>
              <h2 className="section-heading">Glowing engineering capabilities</h2>
            </div>
            <p className="max-w-xl text-sm text-slate-400">
              Organized by categories that reflect real hardware, software, and embedded work.
            </p>
          </div>

          <div className="mt-10 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
            {skillGroups.map((group) => (
              <motion.div
                key={group.title}
                whileHover={{ y: -6 }}
                className="glass-panel border-violet/20 p-6"
              >
                <div className="flex items-center justify-between gap-4">
                  <div>
                    <p className="text-xs uppercase tracking-[0.3em] text-violetSoft">{group.title}</p>
                    <p className="mt-3 text-2xl font-semibold text-white">{group.level}%</p>
                  </div>
                  <div className="rounded-full bg-white/10 px-4 py-2 text-sm text-slate-200">Top</div>
                </div>
                <div className="mt-6 h-3 overflow-hidden rounded-full bg-white/10">
                  <div className="h-full rounded-full bg-gradient-to-r from-violet to-violetSoft" style={{ width: `${group.level}%` }} />
                </div>
                <div className="mt-6 space-y-2 text-sm text-slate-300">
                  {group.items.map((item) => (
                    <div key={item} className="flex items-center gap-3">
                      <span className="h-2.5 w-2.5 rounded-full bg-gold" />
                      <span>{item}</span>
                    </div>
                  ))}
                </div>
              </motion.div>
            ))}
          </div>
        </section>

        <section id="projects" ref={(el) => (sectionsRef.current.projects = el)} className="mt-24">
          <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
            <div>
              <p className="section-subtitle">Projects</p>
              <h2 className="section-heading">Showcase of premium work</h2>
            </div>
            <span className="badge-pill">Futuristic engineering</span>
          </div>

          <div className="mt-10 grid gap-6 xl:grid-cols-3">
            {featuredProjects.map((project) => (
              <motion.article
                key={project.title}
                whileHover={{ y: -8 }}
                className="glass-panel border border-violet/20 p-8"
              >
                <div className="flex items-center justify-between gap-4">
                  <div>
                    <p className="text-sm uppercase tracking-[0.3em] text-violetSoft">Featured</p>
                    <h3 className="mt-3 text-2xl font-semibold text-white">{project.title}</h3>
                  </div>
                  <span className="rounded-full bg-gold/10 px-3 py-2 text-sm font-semibold text-gold">Elite</span>
                </div>
                <p className="mt-6 text-slate-300 leading-7">{project.description}</p>
                <div className="mt-6 flex flex-wrap gap-2">
                  {project.tags.map((tag) => (
                    <span key={tag} className="badge-pill border-white/10 bg-white/5 text-slate-200">
                      {tag}
                    </span>
                  ))}
                </div>
                <a
                  href={project.github}
                  target="_blank"
                  rel="noreferrer"
                  className="button-secondary mt-6 inline-flex items-center gap-2"
                >
                  <Github size={16} /> View GitHub
                </a>
              </motion.article>
            ))}
          </div>
        </section>

        <section id="tinkercad" ref={(el) => (sectionsRef.current.tinkercad = el)} className="mt-24 space-y-10">
          <div className="glass-panel border-violet/20 p-8">
            <div className="grid gap-6 lg:grid-cols-[1.1fr_0.9fr] lg:items-center">
              <div>
                <p className="section-subtitle">Tinkercad Projects</p>
                <h2 className="section-heading">Sensors & Actuators Lab</h2>
                <p className="mt-4 max-w-3xl text-slate-300 leading-8">
                  Dynamically sourced from GitHub, this lab dashboard lets recruiters and mentors explore each folder, filter sensor and actuator work, and review real portfolio experiments.
                </p>
              </div>
              <div className="grid gap-4 sm:grid-cols-3">
                <div className="rounded-[28px] border border-violet/20 bg-[#0e0a18]/90 p-5 text-center">
                  <p className="text-sm uppercase tracking-[0.28em] text-violetSoft">Total</p>
                  <p className="mt-4 text-4xl font-semibold text-white">{totalProjects}</p>
                </div>
                <div className="rounded-[28px] border border-violet/20 bg-[#0e0a18]/90 p-5 text-center">
                  <p className="text-sm uppercase tracking-[0.28em] text-violetSoft">Sensors</p>
                  <p className="mt-4 text-4xl font-semibold text-white">{totalSensors}</p>
                </div>
                <div className="rounded-[28px] border border-violet/20 bg-[#0e0a18]/90 p-5 text-center">
                  <p className="text-sm uppercase tracking-[0.28em] text-violetSoft">Actuators</p>
                  <p className="mt-4 text-4xl font-semibold text-white">{totalActuators}</p>
                </div>
              </div>
            </div>
          </div>

          <div className="grid gap-6 xl:grid-cols-[0.7fr_1.3fr]">
            <div className="glass-panel border-violet/20 p-6">
              <div className="flex items-center justify-between gap-3">
                <div>
                  <p className="text-sm uppercase tracking-[0.28em] text-violetSoft">Search</p>
                  <h3 className="mt-2 text-2xl font-semibold text-white">Filter the lab library</h3>
                </div>
                <span className="rounded-full bg-gold/15 px-4 py-2 text-sm font-semibold text-gold">Live data</span>
              </div>
              <div className="mt-6 space-y-5">
                <label className="block text-sm text-slate-300">
                  Search projects
                  <div className="mt-3 rounded-3xl border border-white/10 bg-[#0d091a] px-4 py-3 shadow-inner">
                    <Search size={16} className="inline-block text-violet" />
                    <input
                      type="search"
                      value={searchQuery}
                      onChange={(event) => setSearchQuery(event.target.value)}
                      placeholder="Search by name, type, or keyword"
                      className="ml-3 w-full bg-transparent text-white outline-none placeholder:text-slate-500"
                    />
                  </div>
                </label>
                <div className="grid gap-3 md:grid-cols-3">
                  {[
                    { id: "all", label: "All Projects" },
                    { id: "sensors", label: "Sensors" },
                    { id: "actuators", label: "Actuators" }
                  ].map((option) => (
                    <button
                      key={option.id}
                      onClick={() => setStatusFilter(option.id)}
                      className={`rounded-3xl border px-4 py-3 text-left text-sm transition ${
                        statusFilter === option.id
                          ? "border-gold bg-gold/10 text-gold"
                          : "border-white/10 bg-white/5 text-slate-300 hover:bg-white/10"
                      }`}
                    >
                      {option.label}
                    </button>
                  ))}
                </div>
                <p className="text-sm text-slate-400">
                  {filteredTinkercad.length} project cards visible based on search and filter.
                </p>
              </div>
            </div>

            <div className="glass-panel border-violet/20 p-6">
              <p className="text-sm uppercase tracking-[0.28em] text-violetSoft">How it works</p>
              <h3 className="mt-3 text-2xl font-semibold text-white">GitHub-driven project discovery</h3>
              <p className="mt-4 text-slate-300 leading-7">
                This dashboard scans every folder in the sensors and actuators repository, generates summaries, and displays each lab as a premium card.
              </p>
              <div className="mt-6 rounded-[28px] border border-white/10 bg-[#0d0917]/90 p-6">
                <div className="flex items-start gap-3">
                  <Sparkles size={20} className="text-violet" />
                  <div>
                    <p className="font-semibold text-white">Live repository sync</p>
                    <p className="mt-2 text-sm text-slate-400">Projects are derived directly from folders in GitHub.</p>
                  </div>
                </div>
                <div className="mt-5 flex flex-wrap gap-2">
                  <span className="badge-pill border-white/10 bg-white/5 text-slate-200">GitHub API</span>
                  <span className="badge-pill border-white/10 bg-white/5 text-slate-200">Smart filtering</span>
                  <span className="badge-pill border-white/10 bg-white/5 text-slate-200">Auto summaries</span>
                </div>
              </div>
            </div>
          </div>

          {tinkercadLoading ? (
            <div className="glass-panel border-violet/20 p-8 text-center text-slate-300">Loading projects...</div>
          ) : tinkercadError ? (
            <div className="glass-panel border-violet/20 p-8 text-center text-orange-300">{tinkercadError}</div>
          ) : (
            <div className="grid gap-6 xl:grid-cols-3">
              {filteredTinkercad.map((project) => {
                const Icon = project.Icon;
                return (
                  <motion.article
                    key={project.id}
                    whileHover={{ y: -6 }}
                    className="glass-panel border border-violet/20 p-6"
                  >
                    <div className="flex items-center justify-between gap-4">
                      <div className="flex items-center gap-4">
                        <div className="grid h-14 w-14 place-items-center rounded-3xl bg-violet/10 text-violetSoft">
                          <Icon size={24} />
                        </div>
                        <div>
                          <p className="text-xs uppercase tracking-[0.28em] text-violetSoft">{project.projectType}</p>
                          <h4 className="mt-2 text-xl font-semibold text-white">{project.title}</h4>
                        </div>
                      </div>
                      <span className="badge-pill border-gold/20 bg-gold/10 text-gold">Verified</span>
                    </div>
                    <p className="mt-5 text-slate-300 leading-7">{project.description}</p>
                    <a
                      href={project.githubUrl}
                      target="_blank"
                      rel="noreferrer"
                      className="button-secondary mt-6 inline-flex items-center gap-2"
                    >
                      <Github size={16} /> View folder
                    </a>
                  </motion.article>
                );
              })}
            </div>
          )}
        </section>

        <section id="contact" ref={(el) => (sectionsRef.current.contact = el)} className="mt-24">
          <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
            <div>
              <p className="section-subtitle">Contact</p>
              <h2 className="section-heading">Premium contact panel</h2>
            </div>
            <span className="badge-pill border-white/10 bg-white/5">Reach out in violet + gold</span>
          </div>

          <div className="grid gap-6 xl:grid-cols-[1.05fr_0.95fr]">
            <motion.div
              initial={{ opacity: 0, y: 28 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.2 }}
              className="glass-panel border-violet/20 p-8"
            >
              <p className="text-sm uppercase tracking-[0.28em] text-violetSoft">Get in touch</p>
              <h3 className="mt-4 text-3xl font-semibold text-white">Engineering transforms ideas into innovation.</h3>
              <p className="mt-4 text-slate-300 leading-8">
                I’m available for internships, research support, and collaborative hardware projects. Send a message to explore how we can build refined IoT systems together.
              </p>
              <form action="mailto:mahimasj07@gmail.com" className="mt-8 grid gap-5">
                <input type="text" placeholder="Name" className="input-glass" />
                <input type="email" placeholder="Email" className="input-glass" />
                <textarea placeholder="Message" className="input-glass min-h-[160px] resize-none" />
                <button type="submit" className="button-primary w-full justify-center">
                  Send Message
                </button>
              </form>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 28 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.2 }}
              className="glass-panel border-violet/20 p-8"
            >
              <p className="text-sm uppercase tracking-[0.28em] text-violetSoft">Contact details</p>
              <div className="mt-8 space-y-4 text-slate-300">
                <ContactRow icon={Mail} label="Email" value="mahimasj07@gmail.com" href="mailto:mahimasj07@gmail.com" />
                <ContactRow icon={Linkedin} label="LinkedIn" value="linkedin.com/in/mahimasj07" href="https://www.linkedin.com/in/mahimasj07" />
                <ContactRow icon={Github} label="GitHub" value="github.com/mahimasj07" href="https://github.com/mahimasj07/neon-mermaid" />
              </div>
            </motion.div>
          </div>
        </section>

        <footer className="mt-24 rounded-[36px] border border-white/10 bg-[#09060f]/80 p-8 text-slate-400 shadow-glow backdrop-blur-3xl sm:p-10">
          <div className="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">
            <div className="space-y-3">
              <p className="uppercase tracking-[0.28em] text-violetSoft">Final note</p>
              <p className="text-2xl font-semibold text-white">Engineering transforms ideas into innovation.</p>
            </div>
            <div className="flex flex-wrap items-center gap-4 text-sm text-slate-300">
              <a href="https://github.com/mahimasj07/neon-mermaid" target="_blank" rel="noreferrer" className="hover:text-white">
                GitHub
              </a>
              <a href="https://www.linkedin.com/in/mahimasj07" target="_blank" rel="noreferrer" className="hover:text-white">
                LinkedIn
              </a>
              <a href="#contact" className="hover:text-white">
                Contact
              </a>
            </div>
          </div>
        </footer>
      </main>
    </div>
  );
}

function ContactRow({ icon: Icon, label, value, href }) {
  return (
    <a
      href={href}
      target="_blank"
      rel="noreferrer"
      className="flex items-center justify-between gap-4 rounded-3xl border border-white/10 bg-white/5 px-5 py-4 transition hover:border-gold hover:text-gold"
    >
      <div className="flex items-center gap-3">
        <span className="grid h-12 w-12 place-items-center rounded-3xl bg-violet/10 text-violetSoft">
          <Icon size={18} />
        </span>
        <div className="space-y-1 text-left">
          <p className="text-sm uppercase tracking-[0.24em] text-violetSoft">{label}</p>
          <p className="text-base font-semibold text-white">{value}</p>
        </div>
      </div>
      <ExternalLink size={16} />
    </a>
  );
}

createRoot(document.getElementById("root")).render(<App />);
'''
css = '''@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

  html {
    scroll-behavior: smooth;
  }

  body {
    @apply min-h-screen bg-[#050505] text-white antialiased;
    font-family: 'Inter', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background-image: radial-gradient(circle at top left, rgba(124, 58, 237, 0.18), transparent 22%),
      radial-gradient(circle at 80% 12%, rgba(255, 215, 0, 0.12), transparent 18%),
      linear-gradient(180deg, #050505 0%, #0a0314 55%, #110a1f 100%);
  }

  * {
    box-sizing: border-box;
  }

  ::selection {
    @apply bg-violet/40 text-white;
  }
}

@layer components {
  .glass-panel {
    @apply rounded-[36px] border border-white/10 bg-white/5 backdrop-blur-3xl shadow-glow;
  }

  .button-primary {
    @apply inline-flex items-center justify-center gap-2 rounded-full bg-gradient-to-r from-violet to-violetSoft px-6 py-3 text-sm font-semibold text-black transition duration-300 hover:-translate-y-0.5 hover:shadow-gold;
  }

  .button-secondary {
    @apply inline-flex items-center justify-center gap-2 rounded-full border border-white/10 bg-white/5 px-6 py-3 text-sm font-semibold text-white transition duration-300 hover:bg-white/10;
  }

  .badge-pill {
    @apply inline-flex items-center rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs uppercase tracking-[0.24em] text-slate-200;
  }

  .input-glass {
    @apply w-full rounded-[28px] border border-white/10 bg-[#0d0917]/90 px-5 py-4 text-sm text-white outline-none transition duration-300 placeholder:text-slate-500 focus:border-violet/50 focus:ring-2 focus:ring-violet/20;
  }
}

@layer utilities {
  .shadow-glow {
    box-shadow: 0 30px 90px rgba(124, 58, 237, 0.22);
  }

  .shadow-gold {
    box-shadow: 0 22px 48px rgba(255, 215, 0, 0.22);
  }

  .orb {
    position: absolute;
    border-radius: 9999px;
    opacity: 0.45;
    filter: blur(60px);
    animation: float 12s ease-in-out infinite;
  }

  .particle {
    position: absolute;
    border-radius: 9999px;
    background: rgba(255, 255, 255, 0.65);
    opacity: 0.75;
    width: 0.4rem;
    height: 0.4rem;
    animation: drift 10s ease-in-out infinite;
  }
}

@keyframes float {
  0%,
  100% {
    transform: translateY(0px) scale(1);
  }
  50% {
    transform: translateY(-16px) scale(1.04);
  }
}

@keyframes drift {
  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }
  50% {
    transform: translate(12px, -18px) scale(1.1);
  }
}
'''
Path('src/main.jsx').write_text(main, encoding='utf-8')
Path('src/styles.css').write_text(css, encoding='utf-8')
