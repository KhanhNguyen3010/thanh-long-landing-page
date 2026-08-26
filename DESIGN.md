---
name: Global Horizon
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#424750'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#737781'
  outline-variant: '#c3c6d2'
  surface-tint: '#305ea0'
  primary: '#002a58'
  on-primary: '#ffffff'
  primary-container: '#004080'
  on-primary-container: '#83aef5'
  inverse-primary: '#a9c7ff'
  secondary: '#944a00'
  on-secondary: '#ffffff'
  secondary-container: '#fc8f34'
  on-secondary-container: '#663100'
  tertiary: '#003216'
  on-tertiary: '#ffffff'
  tertiary-container: '#004b24'
  on-tertiary-container: '#42c372'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#a9c7ff'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#0e4686'
  secondary-fixed: '#ffdcc5'
  secondary-fixed-dim: '#ffb783'
  on-secondary-fixed: '#301400'
  on-secondary-fixed-variant: '#713700'
  tertiary-fixed: '#7efba4'
  tertiary-fixed-dim: '#61de8a'
  on-tertiary-fixed: '#00210c'
  on-tertiary-fixed-variant: '#005228'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
  trust-blue-dark: '#002B56'
  amber-soft: '#FFF4E6'
  success-green-light: '#EBF7ED'
  ink-black: '#0F172A'
  slate-gray: '#64748B'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-md:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-sm:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  section-padding: 80px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
The design system is built on a foundation of **Corporate Modernism**, emphasizing reliability, international prestige, and human-centric service. Given the life-changing nature of overseas study and labor migration, the UI must evoke confidence and institutional stability while remaining welcoming to applicants from diverse backgrounds.

The aesthetic utilizes clean lines, generous whitespace, and a structured information hierarchy to convey transparency. By blending professional precision with soft UI elements, the design system strikes a balance between a high-stakes legal consultancy and a supportive career partner.

## Colors
The palette is rooted in a deep **Primary Blue (#004080)**, chosen for its traditional association with trust, authority, and the global corporate landscape. This is the dominant color for headers, primary actions, and structural anchors.

**Secondary Orange/Amber** acts as the primary accent, used for Call-to-Action (CTA) elements to provide warmth and visibility without sacrificing professionalism. **Tertiary Green** is reserved for success states, "approved" visa statuses, and financial growth indicators. The background uses a very soft **Neutral Slate (#F8FAFC)** to reduce eye strain and provide a premium, clean canvas for content.

## Typography
The typography strategy pairs **Montserrat** for headings with **Inter** for body text. Montserrat provides a geometric, modern, and confident look that feels established and international. Inter was selected for its exceptional legibility in data-heavy sections, such as program requirements and legal disclosures.

- **Headlines:** Use Montserrat Bold/SemiBold with tight letter-spacing for a high-impact, professional feel.
- **Body Text:** Use Inter Regular. Increase line height to 1.6 for long-form consultancy descriptions to ensure readability.
- **System Labels:** Use Inter SemiBold in uppercase for "Quick Facts" or "Status Labels" (e.g., "BAY NHANH", "LƯƠNG CAO").

## Layout & Spacing
This design system utilizes a **12-column fixed grid** for desktop, ensuring that information-heavy "Program Cards" remain organized and legible. On mobile devices, the layout shifts to a single-column fluid flow with 16px side margins.

- **Information Density:** Medium. Use generous `section-padding` (80px) to separate distinct stages of the workflow (About Us vs. Core Services).
- **Rhythm:** Use an 8px base grid. All margins and paddings should be multiples of 8 to maintain a rigorous, professional alignment.
- **Grids:** Programs should be displayed in a 3-column grid on desktop and a 1-column stack on mobile to focus the user's attention on specific opportunities.

## Elevation & Depth
To maintain a "reliable and institutional" feel, the design system avoids heavy shadows or distracting gradients. Instead, it uses **Tonal Layers** and **Soft Ambient Shadows**.

- **Surface Levels:** The main background is Neutral. Elevated cards (Programs, Testimonials) use a pure white (#FFFFFF) background with a very subtle 1px border (#E2E8F0) and a soft, low-opacity shadow (0px 4px 20px rgba(0, 0, 0, 0.05)).
- **Interactivity:** On hover, cards may lift slightly with a more pronounced shadow to indicate clickability.
- **Navigation:** The Header is sticky and uses a semi-transparent white background with a backdrop-blur (10px) to maintain context as the user scrolls through the lengthy landing page.

## Shapes
A **Soft (0.25rem)** roundedness is applied to standard UI elements. This level of rounding removes the "sharpness" of a purely utilitarian system, making it feel more approachable and modern without appearing too casual or "bubbly."

- **Standard Buttons/Inputs:** 4px (0.25rem) radius.
- **Large Cards/Images:** 8px (0.5rem) radius for a more substantial, container-like feel.
- **Featured Chips:** Pill-shaped (fully rounded) for status indicators like "HOT" or "NEW" to make them stand out from the rectangular grid.

## Components

### Buttons
- **Primary:** Solid Primary Blue background with White text. Bold, professional, and high contrast.
- **Secondary (CTA):** Solid Secondary Orange background. Reserved specifically for "Consultation" and "Enroll Now" actions.
- **Ghost:** Primary Blue border with transparent background. Used for "Learn More" or secondary navigations.

### Program Cards
Cards must include a header image of the destination country, a Primary Blue title, and a structured list of "Quick Facts" (Salary, Duration, Requirements). Use a Tertiary Green badge for income highlights.

### Timeline (Workflow)
A vertical or horizontal line (Primary Blue, 2px thickness) connecting numbered nodes. Each node should contain a simple icon and a short description.

### Input Fields
Clean, outlined fields with Slate-Gray borders. On focus, the border transitions to Primary Blue. Include clear placeholder text and validation icons to assist applicants in filling out the form accurately.

### FAQ Accordion
A flat design with a subtle border. Use Montserrat SemiBold for questions. The toggle icon should be a simple chevron that rotates 180 degrees upon expansion.

### Testimonials
A simple carousel featuring a circular avatar, the applicant's name in Label-Bold, and the quote in Body-MD italics. Include the country flag or program name as a small subtitle.