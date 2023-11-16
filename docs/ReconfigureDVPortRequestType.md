# ReconfigureDVPortRequestType

The parameters of *DistributedVirtualSwitch.ReconfigureDVPort_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | [**List[DVPortConfigSpec]**](DVPortConfigSpec.md) | The specification of the ports.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.reconfigure_dv_port_request_type import ReconfigureDVPortRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureDVPortRequestType from a JSON string
reconfigure_dv_port_request_type_instance = ReconfigureDVPortRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigureDVPortRequestType.to_json()

# convert the object into a dict
reconfigure_dv_port_request_type_dict = reconfigure_dv_port_request_type_instance.to_dict()
# create an instance of ReconfigureDVPortRequestType from a dict
reconfigure_dv_port_request_type_form_dict = reconfigure_dv_port_request_type.from_dict(reconfigure_dv_port_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


