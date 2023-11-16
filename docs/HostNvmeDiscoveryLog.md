# HostNvmeDiscoveryLog

This data object represents the Discovery Log returned by an NVME over Fabrics Discovery controller.  The Discovery Log consists of pages which contain a number of entries. It provides an inventory of NVM subsystems with which the host may attempt to form an association through an NVME over Fabrics adapter. For details, see: - \"NVM Express over Fabrics 1.0\", Section 5.3,   Discovery Log Page    ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**List[HostNvmeDiscoveryLogEntry]**](HostNvmeDiscoveryLogEntry.md) | The list of entries that make up the Discovery Log.  ***Since:*** vSphere API 7.0  | [optional] 
**complete** | **bool** | Indicates whether the NvmeDiscoveryLog object completely represents the underlying Discovery Log returned by the controller.  It is possible some of the entries returned by the Discovery Controller contain unsupported transport types or data that cannot be interpreted - in that case, those entries will be skipped and the log will be marked as incomplete.  ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.host_nvme_discovery_log import HostNvmeDiscoveryLog

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeDiscoveryLog from a JSON string
host_nvme_discovery_log_instance = HostNvmeDiscoveryLog.from_json(json)
# print the JSON string representation of the object
print HostNvmeDiscoveryLog.to_json()

# convert the object into a dict
host_nvme_discovery_log_dict = host_nvme_discovery_log_instance.to_dict()
# create an instance of HostNvmeDiscoveryLog from a dict
host_nvme_discovery_log_form_dict = host_nvme_discovery_log.from_dict(host_nvme_discovery_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


