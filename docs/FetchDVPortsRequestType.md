# FetchDVPortsRequestType

The parameters of *DistributedVirtualSwitch.FetchDVPorts*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | [**DistributedVirtualSwitchPortCriteria**](DistributedVirtualSwitchPortCriteria.md) |  | [optional] 

## Example

```python
from vmware_vi.models.fetch_dv_ports_request_type import FetchDVPortsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FetchDVPortsRequestType from a JSON string
fetch_dv_ports_request_type_instance = FetchDVPortsRequestType.from_json(json)
# print the JSON string representation of the object
print FetchDVPortsRequestType.to_json()

# convert the object into a dict
fetch_dv_ports_request_type_dict = fetch_dv_ports_request_type_instance.to_dict()
# create an instance of FetchDVPortsRequestType from a dict
fetch_dv_ports_request_type_form_dict = fetch_dv_ports_request_type.from_dict(fetch_dv_ports_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


