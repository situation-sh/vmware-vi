# PerfProviderSummary

This data object type contains information about a performance provider, the type of statistics it generates, and the *PerfProviderSummary.refreshRate* for statistics generation.  A performance provider is any *managed object* that generates real-time or historical statistics (or both&#151;the *PerfProviderSummary.currentSupported* and *PerfProviderSummary.summarySupported* properties are not mutually exclusive). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**current_supported** | **bool** | True if this entity supports real-time (current) statistics; false if it does not.  If this property is true for an entity, a client application can set the *PerfQuerySpec.intervalId* of the *PerfQuerySpec* (passed to the *PerformanceManager.QueryPerf* operation) to the *PerfProviderSummary.refreshRate* to obtain the maximum information possible for the entity.  | 
**summary_supported** | **bool** | True if this entity supports historical (aggregated) statistics; false if it does not.  When this property is true for an entity, a client application can set the *PerfQuerySpec.intervalId* of *PerformanceManager.QueryPerf* to one of the historical *intervals* to obtain historical statistics for this entity.  | 
**refresh_rate** | **int** | Number of seconds between the generation of each counter.  This value applies only to entities that support real-time (current) statistics&amp;#46;  | [optional] 

## Example

```python
from vmware_vi.models.perf_provider_summary import PerfProviderSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PerfProviderSummary from a JSON string
perf_provider_summary_instance = PerfProviderSummary.from_json(json)
# print the JSON string representation of the object
print PerfProviderSummary.to_json()

# convert the object into a dict
perf_provider_summary_dict = perf_provider_summary_instance.to_dict()
# create an instance of PerfProviderSummary from a dict
perf_provider_summary_form_dict = perf_provider_summary.from_dict(perf_provider_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


