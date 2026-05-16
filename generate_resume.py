from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.platypus.flowables import Flowable

NAVY    = colors.HexColor('#1a1a2e')
PINK    = colors.HexColor('#f98ca4')
DARKRED = colors.HexColor('#9e132c')
MUTED   = colors.HexColor('#555555')
BLUE    = colors.HexColor('#2f3e9c')
WHITE   = colors.white

PAGE_W, PAGE_H = letter


class Letterhead(Flowable):
    def __init__(self, width):
        Flowable.__init__(self)
        self.width = width
        self.height = 1.2 * inch

    def draw(self):
        c = self.canv
        w, h = self.width, self.height

        c.setFillColor(NAVY)
        c.rect(0, 0, w, h, fill=1, stroke=0)

        c.setFillColor(PINK)
        c.rect(0, 0, 6, h, fill=1, stroke=0)

        cx, cy, r = 0.7 * inch, h / 2, 0.28 * inch
        c.setFillColor(PINK)
        c.circle(cx, cy, r, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.setFont('Helvetica-Bold', 16)
        c.drawCentredString(cx, cy - 5, 'JD')

        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 22)
        c.drawString(1.2 * inch, h / 2 + 4, 'Jesse Daniels')

        c.setFillColor(PINK)
        c.setFont('Helvetica', 10)
        c.drawString(1.2 * inch, h / 2 - 13, 'Digital Product Manager  &  Web Developer')

        right = w - 0.15 * inch
        c.setFillColor(WHITE)
        c.setFont('Helvetica', 8.5)
        c.drawRightString(right, h / 2 + 8,  '812-204-3219')
        c.drawRightString(right, h / 2 - 4,  'jdanielsstudio@gmail.com')
        c.drawRightString(right, h / 2 - 16, 'linkedin.com/in/jesse-daniels  |  jesse-daniels.com')


def section_header(title):
    items = []
    items.append(Spacer(1, 10))
    items.append(HRFlowable(width='100%', thickness=1.5, color=PINK, spaceAfter=4))
    items.append(Paragraph(title, ParagraphStyle(
        'SectionHead', fontName='Helvetica-Bold', fontSize=11,
        textColor=NAVY, spaceAfter=6
    )))
    return items


def bullet(text, indent=0):
    return Paragraph(
        f'<bullet>•</bullet>{text}',
        ParagraphStyle(
            'Bullet', fontName='Helvetica', fontSize=9.5, leading=14,
            textColor=NAVY, leftIndent=indent + 12, firstLineIndent=0,
            spaceAfter=3, bulletIndent=indent
        )
    )


def build_resume():
    output_path = '/Users/jessedaniels/Desktop/Jesse Daniels - Resume.pdf'

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.35 * inch,
        bottomMargin=0.6 * inch,
    )

    body_width = PAGE_W - 1.3 * inch

    normal = ParagraphStyle('Normal', fontName='Helvetica', fontSize=9.5,
                             leading=14, textColor=NAVY, spaceAfter=6)
    job_title = ParagraphStyle('JobTitle', fontName='Helvetica-Bold', fontSize=10.5,
                                textColor=NAVY, spaceAfter=1)
    org_style = ParagraphStyle('Org', fontName='Helvetica-Bold', fontSize=10.5,
                                textColor=BLUE, spaceAfter=1)
    sub_head = ParagraphStyle('SubHead', fontName='Helvetica-Bold', fontSize=10,
                               textColor=BLUE, spaceAfter=4)
    edu_inst = ParagraphStyle('EduInst', fontName='Helvetica-Bold', fontSize=10,
                               textColor=BLUE, spaceAfter=1)
    edu_deg = ParagraphStyle('EduDeg', fontName='Helvetica-Bold', fontSize=9.5,
                              textColor=NAVY, spaceAfter=2)
    edu_detail = ParagraphStyle('EduDetail', fontName='Helvetica', fontSize=9,
                                 textColor=MUTED, leading=13, spaceAfter=8)
    date_style = ParagraphStyle('Date', fontName='Helvetica', fontSize=9.5,
                                 textColor=MUTED, alignment=2)

    story = []

    # Letterhead
    story.append(Letterhead(body_width))
    story.append(Spacer(1, 0.05 * inch))
    story.append(HRFlowable(width='100%', thickness=2, color=PINK, spaceAfter=10))

    # Summary
    story.append(Paragraph(
        'Business-minded problem solver turned Digital Product Owner &amp; Web Developer, with years '
        'of experience owning and operating successful businesses in the photography industry. My '
        'hands-on background in sales and client relations is now the foundation I use to create '
        'technology that is both intuitive and impactful. Driven by a people-first mindset and a '
        'commitment to ongoing learning, I work to solve real-world challenges and deliver measurable, '
        'bottom-line results.',
        normal
    ))

    # Skills
    story.extend(section_header('Skills'))

    col_left = [
        Paragraph('Product &amp; Project Management', sub_head),
        bullet('Product Ownership &amp; Roadmapping'),
        bullet('Agile Methodology'),
        bullet('Atlassian (Jira, Confluence)'),
        bullet('Stakeholder Presentations &amp; Reporting'),
        bullet('Cross-Functional Leadership: aligning engineering, design, and marketing teams from concept to launch'),
    ]

    col_right = [
        Paragraph('Technical Development &amp; Design', sub_head),
        bullet('Front-End Web Development: HTML, CSS'),
        bullet('Web Accessibility (a11y) Best Practices &amp; WCAG Compliance'),
        bullet('UX/UI Design Principles &amp; Execution'),
        bullet('Graphic &amp; Multimedia Design with Adobe Creative Suite'),
        bullet('Content Management Systems: WordPress, Moodle, SharePoint'),
    ]

    col_w = body_width / 2 - 6
    skills_table = Table(
        [[col_left, col_right]],
        colWidths=[col_w, col_w],
        hAlign='LEFT'
    )
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(skills_table)

    story.append(Spacer(1, 6))
    story.append(Paragraph('Business &amp; Client Relations', sub_head))
    story.append(bullet('Full-Cycle Sales &amp; Client Acquisition | Client-Focused Strategy'))
    story.append(bullet('Exceptional verbal and written skills; adept at delivering compelling presentations and building trust as a strategic partner'))
    story.append(bullet('Experience in translating complex business needs into clear technical requirements and user stories'))

    # Work History
    story.extend(section_header('Work History'))

    # KET
    ket_row = Table(
        [[Paragraph('Kentucky Education Television (KET)', org_style),
          Paragraph('2021 - Present', date_style)]],
        colWidths=[body_width * 0.72, body_width * 0.28],
        hAlign='LEFT'
    )
    ket_row.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(ket_row)
    story.append(Paragraph('Digital Product Manager &amp; Web Developer II', job_title))
    story.append(bullet('Lead the creation of Web Tools, KET\'s intranet platform, from naming, design, to development, collaborating with production, education, graphics, and marketing teams to deliver tools that streamline workflows'))
    story.append(bullet('Drive full product life cycles from concept through launch ensuring alignment with organizational goals'))
    story.append(bullet('Develop and maintain custom WordPress, Moodle, &amp; other content management systems'))
    story.append(bullet('Spearheaded the redesign and launch of KET.org as well as the e-commerce platform Shop.KET.org'))
    story.append(bullet('Chosen as co-lead for the Marketing &amp; Web Development task force to improve cross-team collaboration'))
    story.append(bullet('Initiated and implemented "Scholar Week" sprint rotations to foster ongoing team learning and innovation'))
    story.append(Spacer(1, 8))

    # Photography
    photo_row = Table(
        [[Paragraph('Jesse Daniels Photography LLC', org_style),
          Paragraph('2008 - 2021', date_style)]],
        colWidths=[body_width * 0.72, body_width * 0.28],
        hAlign='LEFT'
    )
    photo_row.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(photo_row)
    story.append(Paragraph('Business Owner &amp; Manager', job_title))
    story.append(bullet('Founded and scaled a full-service production studio, overseeing sales, client relations, and project execution'))
    story.append(bullet('Hired, trained, and managed a team of 14 employees while personally directing over 1,000 events'))
    story.append(bullet('Built a reputation for exceptional client relationships, strategic planning, and creative problem-solving, resulting in sustained business growth for over a decade'))

    # Education
    story.extend(section_header('Education'))

    story.append(Paragraph('Code Louisville  |  Louisville, KY', edu_inst))
    story.append(Paragraph('Full-Stack Development Certificate', edu_deg))
    story.append(Paragraph(
        'Completed an intensive 15-month programming bootcamp with focused certificates in '
        'Front-End Web Development (HTML, CSS, JavaScript), C#, and JavaScript.',
        edu_detail
    ))

    story.append(Paragraph('University of Evansville', edu_inst))
    story.append(Paragraph('Bachelor of Arts in Philosophy', edu_deg))
    story.append(Paragraph(
        'Cultivated a strong foundation in critical thinking, ethical reasoning, and logical analysis. '
        'Emphasis in Technologies, Art, and Business, aligning coursework with early professional interests.',
        edu_detail
    ))

    # Footer
    story.append(Spacer(1, 0.15 * inch))
    story.append(HRFlowable(width='100%', thickness=1, color=PINK, spaceAfter=4))
    story.append(Paragraph(
        'jesse-daniels.com  |  jdanielsstudio@gmail.com  |  812-204-3219',
        ParagraphStyle('Footer', fontName='Helvetica', fontSize=8, textColor=MUTED, alignment=1)
    ))

    doc.build(story)
    print(f'Saved: {output_path}')


build_resume()
