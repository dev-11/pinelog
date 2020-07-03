import unittest
from pinelog import build_invocation_log_entry, build_leave_log_entry, build_exception_log_entry, LogType, LogLevel
from pinelog import constants as c

class LogBuilderTests(unittest.TestCase):
    def test_build_invocation_log_entry_returns_correct_data(self):
        log_entry = build_invocation_log_entry('test_class_name', 'test_method', 123)
        self.assertEqual(LogType.Invoke, log_entry.log_type)
        self.assertEqual(LogLevel.Information, log_entry.log_level)
        self.assertEqual('test_class_name', log_entry.payload[c.PayloadKeys.ClassNameKey])
        self.assertEqual('test_method', log_entry.payload[c.PayloadKeys.MethodKey])
        self.assertEqual(123, log_entry.payload[c.PayloadKeys.ArgsKey])

    def test_build_leave_log_entry_returns_correct_data(self):
        log_entry = build_leave_log_entry('test_class_name', 'test_method', 123)
        self.assertEqual(LogType.Leave, log_entry.log_type)
        self.assertEqual(LogLevel.Information, log_entry.log_level)
        self.assertEqual('test_class_name', log_entry.payload[c.PayloadKeys.ClassNameKey])
        self.assertEqual('test_method', log_entry.payload[c.PayloadKeys.MethodKey])
        self.assertEqual(123, log_entry.payload[c.PayloadKeys.ReturnValueKey])

    def test_build_exception_log_entry_returns_correct_data(self):
        log_entry = build_exception_log_entry('test_class_name', 'test_method', 123)
        self.assertEqual(LogType.Exception, log_entry.log_type)
        self.assertEqual(LogLevel.Error, log_entry.log_level)
        self.assertEqual('test_class_name', log_entry.payload[c.PayloadKeys.ClassNameKey])
        self.assertEqual('test_method', log_entry.payload[c.PayloadKeys.MethodKey])
        self.assertEqual(123, log_entry.payload[c.PayloadKeys.ExceptionKey])