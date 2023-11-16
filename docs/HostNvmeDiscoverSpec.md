# HostNvmeDiscoverSpec

Specifies the parameters necessary to connect to a Discovery Service and retrieve a Discovery Log Page.  Here the transportParameters are used to establish a transport level connection to a Discovery Controller. Further details can be found here: - \"NVM Express over Fabrics 1.0\", Section 5, \"Discovery service\"    ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_connect** | **bool** | Indicates whether the specified adapter should automatically be connected to all the discovered controllers.  It is possible to automatically connect to all discovered controllers. This will only be attempted if this flag is set to true. Whether the connection attempt for an entry succeeded can then be determined via the corresponding *HostNvmeDiscoveryLogEntry.connected* field.  ***Since:*** vSphere API 7.0  | [optional] 
**root_discovery_controller** | **bool** | If set to true, this flag indicates we are connecting to a root/central discovery controller (RDC/CDC).  This will create a persistent connection between the host and the root discovery controller, thus enabling some advanced features.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.host_nvme_discover_spec import HostNvmeDiscoverSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeDiscoverSpec from a JSON string
host_nvme_discover_spec_instance = HostNvmeDiscoverSpec.from_json(json)
# print the JSON string representation of the object
print HostNvmeDiscoverSpec.to_json()

# convert the object into a dict
host_nvme_discover_spec_dict = host_nvme_discover_spec_instance.to_dict()
# create an instance of HostNvmeDiscoverSpec from a dict
host_nvme_discover_spec_form_dict = host_nvme_discover_spec.from_dict(host_nvme_discover_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


