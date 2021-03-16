using Refit;
using GrafanaViewers.StartupManager;
using System.Text.Json;

namespace GrafanaViewers.StartupManager.Refit
{
    public class RefitConfiguration
    {
        public RefitSettings GetConfiguration(JsonSerializerOptions jsonSerializerOptions = null)
        {
            if (jsonSerializerOptions is null)
            {
                jsonSerializerOptions = JsonConfiguration.Get();
                jsonSerializerOptions.IgnoreNullValues = true;
            }

            return new RefitSettings
            {
                ContentSerializer = new SystemTextJsonContentSerializer(jsonSerializerOptions),
                UrlParameterFormatter = new RefitUrlParameterFormatter(),
            };
        }
    }
}