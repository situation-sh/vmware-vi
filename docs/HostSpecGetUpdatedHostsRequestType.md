# HostSpecGetUpdatedHostsRequestType

The parameters of *HostSpecificationManager.HostSpecGetUpdatedHosts*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_change_id** | **str** | The beginning of the time period.  | [optional] 
**end_change_id** | **str** | The ending of the time period.  | [optional] 

## Example

```python
from vmware_vi.models.host_spec_get_updated_hosts_request_type import HostSpecGetUpdatedHostsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostSpecGetUpdatedHostsRequestType from a JSON string
host_spec_get_updated_hosts_request_type_instance = HostSpecGetUpdatedHostsRequestType.from_json(json)
# print the JSON string representation of the object
print HostSpecGetUpdatedHostsRequestType.to_json()

# convert the object into a dict
host_spec_get_updated_hosts_request_type_dict = host_spec_get_updated_hosts_request_type_instance.to_dict()
# create an instance of HostSpecGetUpdatedHostsRequestType from a dict
host_spec_get_updated_hosts_request_type_form_dict = host_spec_get_updated_hosts_request_type.from_dict(host_spec_get_updated_hosts_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


