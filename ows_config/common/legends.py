"""
Shared legend definitions.

BNPB's national hazard convention. Hazard products should render their class
and index bands with these colours rather than choosing their own.
"""

BNPB_HAZARD_CLASSES = (
    {"value": 1, "label": "Rendah", "color": "#1a9850"},
    {"value": 2, "label": "Sedang", "color": "#fee08b"},
    {"value": 3, "label": "Tinggi", "color": "#d73027"},
)

HAZARD_CLASS_LEGEND = {
    "width": 2.0,
    "height": 1.1,
}


def hazard_class_value_map(band):
    """Value-map rules for a hazard class band coded 1/2/3."""
    highest_first = reversed(BNPB_HAZARD_CLASSES)
    return {
        band: [
            {
                "title": hazard_class["label"],
                "values": [hazard_class["value"]],
                "color": hazard_class["color"],
            }
            for hazard_class in highest_first
        ]
    }


def _blend(start, end, position):
    start_rgb = [int(start[i:i + 2], 16) for i in (1, 3, 5)]
    end_rgb = [int(end[i:i + 2], 16) for i in (1, 3, 5)]
    return "#{:02x}{:02x}{:02x}".format(
        *(round(s + (e - s) * position) for s, e in zip(start_rgb, end_rgb))
    )


def hazard_index_color_ramp(breakpoints):
    """Ramp the class colours across the breakpoints, Sedang at mid-scale."""
    low, moderate, high = (hazard_class["color"] for hazard_class in BNPB_HAZARD_CLASSES)
    lowest = breakpoints[0]
    span = breakpoints[-1] - lowest
    ramp = []
    for value in breakpoints:
        position = (value - lowest) / span
        if position <= 0.5:
            color = _blend(low, moderate, position * 2)
        else:
            color = _blend(moderate, high, (position - 0.5) * 2)
        ramp.append({"value": value, "color": color})
    return ramp
