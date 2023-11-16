# HostAccessRestrictedToManagementServer

Fault thrown when an attempt is made to adjust resource settings directly on a host that is being managed by VC.  VC is currently the source of truth for all resource pools on the host. Examples of methods affected by this are: - create respool - update respool - change VM resource settings.     ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**management_server** | **str** | Name/IP of the server currently managing this host.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.host_access_restricted_to_management_server import HostAccessRestrictedToManagementServer

# TODO update the JSON string below
json = "{}"
# create an instance of HostAccessRestrictedToManagementServer from a JSON string
host_access_restricted_to_management_server_instance = HostAccessRestrictedToManagementServer.from_json(json)
# print the JSON string representation of the object
print HostAccessRestrictedToManagementServer.to_json()

# convert the object into a dict
host_access_restricted_to_management_server_dict = host_access_restricted_to_management_server_instance.to_dict()
# create an instance of HostAccessRestrictedToManagementServer from a dict
host_access_restricted_to_management_server_form_dict = host_access_restricted_to_management_server.from_dict(host_access_restricted_to_management_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


