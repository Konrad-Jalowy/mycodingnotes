using System;
using System.Collections.Generic;

class Publisher
{
    private List<Action<string>> _subscribers = new List<Action<string>>();

    public void Subscribe(Action<string> subscriber)
    {
        _subscribers.Add(subscriber);
    }

    public void Unsubscribe(Action<string> subscriber)
    {
        _subscribers.Remove(subscriber);
    }

    public void Notify(string message)
    {
        foreach (var subscriber in _subscribers)
        {
            subscriber(message);
        }
    }
}