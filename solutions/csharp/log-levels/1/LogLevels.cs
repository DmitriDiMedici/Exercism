using System;

static class LogLine
{
    public static string Message(string logLine)
    {
        string[] separators = {":"};
        string[] result = logLine.Split(separators, StringSplitOptions.None);
        return result[1].Trim();
        
    }

    public static string LogLevel(string logLine)
    {
        string[] separators = {"[", "]"};
        string[] result = logLine.Split(separators, StringSplitOptions.None);
        return result[1].Trim().ToLower();
    }

    public static string Reformat(string logLine)
    {
        string[] separators = {"[", "]", ":"};
        string[] result = logLine.Split(separators, StringSplitOptions.None);
        string level = result[1].ToLower();
        string message = result[3].Trim();
        string finalMessage = message + " "+ "(" + level + ")";
        return finalMessage;
    }
}
