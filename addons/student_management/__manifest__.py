# -*- coding: utf-8 -*-
{
    "name": "student_management",
    # TODO
    "summary": """
        student_management""",
    # TODO
    "description": """
        student_management
    """,
    "license": "AGPL-3",
    "author": "Daysum",
    "maintainers": ["angemollou"],
    "website": "https://daysum.net",
    "category": "Services/School",
    "version": "16.0.0.1",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/teacher_views.xml",
        "views/student_views.xml",
        "views/course_views.xml",
        "views/staff_views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "installable": True,
    "application": True,
    "assets": {
        "web.assets_backend": [
            "student_management/static/src/js/double_click_open_fields_backend.js"
        ]
    },
}
