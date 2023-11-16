# VirtualMachineIndependentFilterSpec

The IndependentFilterSpec data object is used to specify the independent filters to be associated with virtual machine disks.  ***Since:*** vSphere API 7.0.2.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_name** | **str** | Name/id of the IO filter.  ***Since:*** vSphere API 7.0.2.1  | 
**filter_class** | **str** | IO filter class.  ***Since:*** vSphere API 7.0.2.1  | [optional] 
**filter_capabilities** | [**List[KeyValue]**](KeyValue.md) | Capabilities defined by the above filter.  Basically this key value pair define the configurable properties of the independent filters. Users can specify desired values.  ***Since:*** vSphere API 7.0.2.1  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_independent_filter_spec import VirtualMachineIndependentFilterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineIndependentFilterSpec from a JSON string
virtual_machine_independent_filter_spec_instance = VirtualMachineIndependentFilterSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineIndependentFilterSpec.to_json()

# convert the object into a dict
virtual_machine_independent_filter_spec_dict = virtual_machine_independent_filter_spec_instance.to_dict()
# create an instance of VirtualMachineIndependentFilterSpec from a dict
virtual_machine_independent_filter_spec_form_dict = virtual_machine_independent_filter_spec.from_dict(virtual_machine_independent_filter_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


