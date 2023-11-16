# VmPoweringOnWithCustomizedDVPortEvent

This event records when a virtual machine was powering on using DVPorts with port level configuration, which might be different from the DVportgroup.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic** | [**List[VnicPortArgument]**](VnicPortArgument.md) | The list of Virtual NIC that were using the DVports.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.vm_powering_on_with_customized_dv_port_event import VmPoweringOnWithCustomizedDVPortEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmPoweringOnWithCustomizedDVPortEvent from a JSON string
vm_powering_on_with_customized_dv_port_event_instance = VmPoweringOnWithCustomizedDVPortEvent.from_json(json)
# print the JSON string representation of the object
print VmPoweringOnWithCustomizedDVPortEvent.to_json()

# convert the object into a dict
vm_powering_on_with_customized_dv_port_event_dict = vm_powering_on_with_customized_dv_port_event_instance.to_dict()
# create an instance of VmPoweringOnWithCustomizedDVPortEvent from a dict
vm_powering_on_with_customized_dv_port_event_form_dict = vm_powering_on_with_customized_dv_port_event.from_dict(vm_powering_on_with_customized_dv_port_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


