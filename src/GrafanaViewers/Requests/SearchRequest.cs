namespace GrafanaViewers.Requests
{
    public abstract class SearchRequest
    {
        public string PanelTitle { get; set; }
        public string Tag { get; set; }
        public string DashboardTitle { get; set; }
        public string TimeOff { get; set; }
    }
}