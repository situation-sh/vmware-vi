# PerfMetricId

This data object type contains information that associates a performance counter with a performance metric.  When constructing this data object for the *PerfQuerySpec.metricId* property of the *PerfQuerySpec* to submit to one of the *PerformanceManager* query operations, the *PerfMetricId.instance* property supports these special characters: - An asterisk (\\*) to specify all instances of the metric for the   specified *PerfMetricId.counterId* - Double-quotes (\"\") to specify aggregated statistics 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter_id** | **int** | The *ID* of the counter for the metric.  | 
**instance** | **str** | An identifier that is derived from configuration names for the device associated with the metric.  It identifies the instance of the metric with its source. This property may be empty. - For memory and aggregated statistics, this property is empty. - For host and virtual machine devices, this property contains the   name of the device, such as the name of the host-bus adapter or   the name of the virtual Ethernet adapter. For example,   &amp;#147;mpx&amp;#46;vmhba33&amp;#58;C0&amp;#58;T0&amp;#58;L0&amp;#148; or   &amp;#147;vmnic0&amp;#58;&amp;#148; - For a CPU, this property identifies the numeric position within   the CPU core, such as 0, 1, 2, 3. - For a virtual disk, this property identifies the file type:   - DISKFILE, for virtual machine base-disk files   - SWAPFILE, for virtual machine swap files   - DELTAFILE, for virtual machine snapshot overhead files   - OTHERFILE, for all other files of a virtual machine  | 

## Example

```python
from vmware_vi.models.perf_metric_id import PerfMetricId

# TODO update the JSON string below
json = "{}"
# create an instance of PerfMetricId from a JSON string
perf_metric_id_instance = PerfMetricId.from_json(json)
# print the JSON string representation of the object
print PerfMetricId.to_json()

# convert the object into a dict
perf_metric_id_dict = perf_metric_id_instance.to_dict()
# create an instance of PerfMetricId from a dict
perf_metric_id_form_dict = perf_metric_id.from_dict(perf_metric_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


