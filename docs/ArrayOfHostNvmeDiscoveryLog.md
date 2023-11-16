# ArrayOfHostNvmeDiscoveryLog

A boxed array of *HostNvmeDiscoveryLog*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNvmeDiscoveryLog]**](HostNvmeDiscoveryLog.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nvme_discovery_log import ArrayOfHostNvmeDiscoveryLog

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNvmeDiscoveryLog from a JSON string
array_of_host_nvme_discovery_log_instance = ArrayOfHostNvmeDiscoveryLog.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNvmeDiscoveryLog.to_json()

# convert the object into a dict
array_of_host_nvme_discovery_log_dict = array_of_host_nvme_discovery_log_instance.to_dict()
# create an instance of ArrayOfHostNvmeDiscoveryLog from a dict
array_of_host_nvme_discovery_log_form_dict = array_of_host_nvme_discovery_log.from_dict(array_of_host_nvme_discovery_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


