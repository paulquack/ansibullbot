#!/usr/bin/env python

import unittest
from ansibullbot.utils.extractors import extract_template_data

# def extract_template_data(
#   body,
#   issue_number=None,
#   issue_class='issue',
#   SECTIONS=SECTIONS
# ):

class TestTemplateExtraction(unittest.TestCase):
    def test_0(self):
        body = [
            '#### ONE',
            'section one',
            '#### TWO',
            'section two',
            '#### THREE',
            'section three'
        ]
        body = '\r\n'.join(body)
        issue_number = 0
        issue_class = 'issue'
        sections = ['ONE', 'TWO', 'THREE']
        tdata = extract_template_data(
            body, issue_number=issue_number,
            issue_class=issue_class, SECTIONS=sections
        )
        assert tdata.get('one') == 'section one'
        assert tdata.get('two') == 'section two'
        assert tdata.get('three') == 'section three'

    def test_1(self):
        body = [
            '#### ISSUE TYPE',
            '- Bug Report',
            '#### COMPONENT NAME',
            'widget module',
            '#### ANSIBLE VERSION',
            '1.9.x'
            '#### SUMMARY',
            'the widget module does not work for me!!!'
        ]
        body = '\r\n'.join(body)
        issue_number = 0
        issue_class = 'issue'
        sections = ['ISSUE TYPE', 'COMPONENT NAME', 'ANSIBLE VERSION', 'SUMMARY']
        tdata = extract_template_data(
            body, issue_number=issue_number,
            issue_class=issue_class, SECTIONS=sections
        )
        assert tdata.get('ansible version') == '1.9.x'
        assert tdata.get('issue type') == 'bug report'
        assert tdata.get('component name') == 'widget'
        assert tdata.get('component_raw') == 'widget module'
        assert tdata.get('summary') == 'the widget module does not work for me!!!'

    # FIXME
    '''
    def test_2(self):
        body = [
            '*** issue type ***:',
            '- Bug Report',
            '*** componet name ***:',
            'widget module',
            '*** ansible version ***:',
            '1.9.x'
            '*** summary ***:',
            'the widget module does not work for me!!!'
        ]
        body = '\r\n'.join(body)
        issue_number = 0
        issue_class = 'issue'
        sections = ['ISSUE TYPE', 'COMPONENT NAME', 'ANSIBLE VERSION', 'SUMMARY']
        tdata = extract_template_data(
            body, issue_number=issue_number,
            issue_class=issue_class, SECTIONS=sections
        )
        assert tdata.get('ansible version') == '1.9.x'
        assert tdata.get('issue type') == 'bug report'
        assert tdata.get('component name') == 'widget'
        assert tdata.get('component_raw') == 'widget module'
        assert tdata.get('summary') == 'the widget module does not work for me!!!'
    '''