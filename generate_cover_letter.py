from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.flowables import Flowable

# Site colors
NAVY    = colors.HexColor('#1a1a2e')
PINK    = colors.HexColor('#f98ca4')
DARKRED = colors.HexColor('#9e132c')
GREEN   = colors.HexColor('#65f283')
MUTED   = colors.HexColor('#555555')
WHITE   = colors.white

PAGE_W, PAGE_H = letter


class Letterhead(Flowable):
    """Draws the full letterhead header block."""

    def __init__(self, width):
        Flowable.__init__(self)
        self.width = width
        self.height = 1.35 * inch

    def draw(self):
        c = self.canv
        w, h = self.width, self.height

        # Navy background bar
        c.setFillColor(NAVY)
        c.rect(0, 0, w, h, fill=1, stroke=0)

        # Pink accent stripe on left edge
        c.setFillColor(PINK)
        c.rect(0, 0, 6, h, fill=1, stroke=0)

        # "JD" monogram circle
        cx, cy, r = 0.75 * inch, h / 2, 0.32 * inch
        c.setFillColor(PINK)
        c.circle(cx, cy, r, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.setFont('Helvetica-Bold', 18)
        c.drawCentredString(cx, cy - 6, 'JD')

        # Name
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 24)
        c.drawString(1.3 * inch, h / 2 + 4, 'Jesse Daniels')

        # Title
        c.setFillColor(PINK)
        c.setFont('Helvetica', 11)
        c.drawString(1.3 * inch, h / 2 - 14, 'Digital Product Manager  &  Web Developer')

        # Contact info right-aligned
        c.setFillColor(WHITE)
        c.setFont('Helvetica', 9)
        right = w - 0.15 * inch
        c.drawRightString(right, h / 2 + 10, 'jdanielsstudio@gmail.com')
        c.drawRightString(right, h / 2 - 4,  'linkedin.com/in/jesse-daniels')
        c.drawRightString(right, h / 2 - 18, 'jesse-daniels.com')


def build_cover_letter():
    output_path = '/Users/jessedaniels/Desktop/Jesse Daniels - Slingshot Cover Letter.pdf'

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.4 * inch,
        bottomMargin=0.75 * inch,
    )

    body_width = PAGE_W - 1.5 * inch

    # Styles
    body_style = ParagraphStyle(
        'Body',
        fontName='Helvetica',
        fontSize=10.5,
        leading=15.5,
        textColor=NAVY,
        spaceBefore=0,
        spaceAfter=8,
    )

    salutation_style = ParagraphStyle(
        'Salutation',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=15.5,
        textColor=NAVY,
        spaceBefore=0,
        spaceAfter=8,
    )

    closing_style = ParagraphStyle(
        'Closing',
        fontName='Helvetica',
        fontSize=11,
        leading=17,
        textColor=NAVY,
        spaceBefore=0,
        spaceAfter=4,
    )

    sig_style = ParagraphStyle(
        'Sig',
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=18,
        textColor=DARKRED,
    )

    paragraphs = [
        "Dear Slingshot Team,",

        "I'm a Digital Product Manager and Web Developer at Kentucky Education Television, and the "
        "Product Lead role reads like a description of work I'm already doing and genuinely love. "
        "I own full product lifecycles, lead cross-functional teams through ambiguity, manage "
        "stakeholder relationships, and ship. I've also been using AI as a real part of my workflow "
        "for years, not because it was trendy, but because it makes the work better.",

        "At KET I led the creation of Web Tools, the organization's internal intranet platform, from "
        "naming through design, development, and launch. I collaborated across production, education, "
        "graphics, and marketing teams to deliver something that actually changed how people work day "
        "to day. I also spearheaded the redesign of KET.org and the launch of Shop.KET.org. These "
        "weren't just technical projects. They required translating ambiguous organizational goals "
        "into clear product decisions, managing competing stakeholder priorities, and keeping teams "
        "aligned on what mattered and why.",

        "On AI: I currently represent the web team on KET's organization wide AI pilot group. The "
        "web team had been using AI for years already. My job in the pilot was to help the broader "
        "organization catch up and find real applications across departments. We are currently "
        "building a custom AI chatbot trained on KET's institutional knowledge that routes support "
        "tickets and, at its best, eliminates help tickets altogether. I also initiated Scholar Week, "
        "a recurring sprint rotation that gives the team dedicated time to learn and experiment. "
        "Teams that build learning into the work build better things.",

        "Before tech I ran a photography business for thirteen years, managed a team of 14, and "
        "directed over 1,000 events. That background taught me to earn client trust fast, make "
        "decisions with imperfect information, and deliver under pressure. Those turned out to be "
        "exactly the skills product work requires.",

        "Slingshot's approach to AI as a core part of how you build, not a bolt-on, is exactly the "
        "environment I want to work in. I'd love to talk.",

        "I also noticed the Product Designer opening. My front-end development background and UX "
        "experience mean I speak that language fluently and can partner closely with your design team "
        "from day one.",
    ]

    story = []

    # Letterhead
    story.append(Letterhead(body_width))
    story.append(Spacer(1, 0.05 * inch))

    # Pink accent rule under header
    story.append(HRFlowable(width='100%', thickness=2, color=PINK, spaceAfter=12))

    # Date
    from datetime import date
    date_style = ParagraphStyle('Date', fontName='Helvetica', fontSize=10,
                                 textColor=MUTED, spaceAfter=10)
    story.append(Paragraph(date.today().strftime('%B %d, %Y'), date_style))

    # Body paragraphs
    for i, text in enumerate(paragraphs):
        style = salutation_style if i == 0 else body_style
        story.append(Paragraph(text, style))

    # Closing
    story.append(Spacer(1, 0.06 * inch))
    story.append(Paragraph('Jesse Daniels', sig_style))
    story.append(Spacer(1, 3))

    closing_detail = ParagraphStyle('ClosingDetail', fontName='Helvetica', fontSize=9,
                                     textColor=MUTED, leading=13)
    story.append(Paragraph('jdanielsstudio@gmail.com  |  linkedin.com/in/jesse-daniels  |  jesse-daniels.com', closing_detail))

    # Footer rule
    story.append(Spacer(1, 0.15 * inch))
    story.append(HRFlowable(width='100%', thickness=1, color=PINK, spaceAfter=4))
    footer_style = ParagraphStyle('Footer', fontName='Helvetica', fontSize=8,
                                   textColor=MUTED, alignment=1)
    story.append(Paragraph('jesse-daniels.com', footer_style))

    doc.build(story)
    print(f'Saved: {output_path}')


build_cover_letter()
