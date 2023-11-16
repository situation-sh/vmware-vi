# GenericDrsFault

DRS returns more than one faults for each virtual machine, or DRS returns *VimFault* because of some internal errors.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_faults** | [**List[MethodFault]**](MethodFault.md) | This is an optional field to return the detailed information back to the client.  This optional array may consist of the exact fault for some hosts in the cluster.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.generic_drs_fault import GenericDrsFault

# TODO update the JSON string below
json = "{}"
# create an instance of GenericDrsFault from a JSON string
generic_drs_fault_instance = GenericDrsFault.from_json(json)
# print the JSON string representation of the object
print GenericDrsFault.to_json()

# convert the object into a dict
generic_drs_fault_dict = generic_drs_fault_instance.to_dict()
# create an instance of GenericDrsFault from a dict
generic_drs_fault_form_dict = generic_drs_fault.from_dict(generic_drs_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


