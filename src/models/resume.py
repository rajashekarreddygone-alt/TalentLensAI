from dataclasses import dataclass, field


@dataclass
class Resume:

    name: str = ""

    email: str = ""

    phone: str = ""

    skills: list = field(default_factory=list)

    education: list = field(default_factory=list)

    experience: list = field(default_factory=list)

    projects: list = field(default_factory=list)

    certifications: list = field(default_factory=list)

    raw_text: str = ""