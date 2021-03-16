using Refit;
using System;
using System.Reflection;

namespace GrafanaViewers.StartupManager.Refit
{
    public class RefitUrlParameterFormatter : DefaultUrlParameterFormatter
    {
        public override string Format(object parameterValue, ICustomAttributeProvider attributeProvider, Type type)
        {
            if (parameterValue is string value && string.IsNullOrWhiteSpace(value))
            {
                return null;
            }

            return base.Format(parameterValue, attributeProvider, type);
        }
    }
}