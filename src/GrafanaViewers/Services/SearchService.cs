using System;
using System.Diagnostics;
using System.Threading.Tasks;
using GrafanaViewers.External;
using GrafanaViewers.Requests;
using Microsoft.Extensions.Logging;

namespace GrafanaViewers.Services
{
    public class SearchService : ISearchService
    {
        private readonly Process _process;
        private readonly IGrafana _grafana;
        private readonly ILogger<ISearchService> _logger;
        private static readonly string secret = Environment.GetEnvironmentVariable("TOKEN_GRAFANA");

        public SearchService(Process process, ILogger<ISearchService> logger, IGrafana grafana)
        {
            _process = process;
            _logger = logger;
            _grafana = grafana;
        }

        public Task<dynamic> Get(SearchRequest request, string operation)
        {
            throw new NotImplementedException();
        }
    }
}