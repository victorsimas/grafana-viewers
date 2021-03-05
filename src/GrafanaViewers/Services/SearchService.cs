using System;
using System.Diagnostics;
using System.Threading.Tasks;
using GrafanaViewers.Requests;
using Microsoft.Extensions.Logging;
using GrafanaViewers.ErrorHandling;

namespace GrafanaViewers.Services
{
    public class SearchService : ISearchService
    {
        private readonly Process _process;
        private readonly ILogger<ISearchService> _logger;

        public SearchService(Process process, ILogger<ISearchService> logger)
        {
            _process = process;
            _logger = logger;
        }

        public Task<dynamic> Get(SearchRequest request, string operation)
        {
            throw new NotImplementedException();
        }
    }
}