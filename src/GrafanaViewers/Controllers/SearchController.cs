using System.Net;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using GrafanaViewers.Requests;
using GrafanaViewers.Services;

namespace GrafanaViewers.Controllers
{
    [ApiController]
    [Route("[controller]")]
    [ProducesResponseType((int)HttpStatusCode.OK)]
    [ProducesResponseType((int)HttpStatusCode.FailedDependency)]
    public class SearchController : ControllerBase
    {
        private readonly ILogger<SearchController> _logger;
        private readonly ISearchService _service;

        public SearchController(ILogger<SearchController> logger, ISearchService service)
        {
            _logger = logger;
            _service = service;
        }

        [HttpGet]
        // [Produces(typeof())]
        public async Task<IActionResult> Get([FromQuery] SearchRequest request)
        {
            return Ok(await Task.FromResult("Okay"));
        }

        [HttpGet("render")]
        // [Produces(typeof())]
        public async Task<IActionResult> GetImage([FromQuery] SearchRequest request)
        {
            return Ok(await Task.FromResult("Okay"));

            
        }
    }
}
