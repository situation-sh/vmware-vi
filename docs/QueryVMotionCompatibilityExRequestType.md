# QueryVMotionCompatibilityExRequestType

The parameters of *VirtualMachineProvisioningChecker.QueryVMotionCompatibilityEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The set of virtual machines to analyze for compatibility. All virtual machines are assumed to be powered-on for the purposes of this operation.  Refers instances of *VirtualMachine*.  | 
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The set of hosts to analyze for compatibility. All hosts are assumed to be connected and not in maintenance mode for the purposes of this operation.  Refers instances of *HostSystem*.  | 

## Example

```python
from vmware_vi.models.query_v_motion_compatibility_ex_request_type import QueryVMotionCompatibilityExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryVMotionCompatibilityExRequestType from a JSON string
query_v_motion_compatibility_ex_request_type_instance = QueryVMotionCompatibilityExRequestType.from_json(json)
# print the JSON string representation of the object
print QueryVMotionCompatibilityExRequestType.to_json()

# convert the object into a dict
query_v_motion_compatibility_ex_request_type_dict = query_v_motion_compatibility_ex_request_type_instance.to_dict()
# create an instance of QueryVMotionCompatibilityExRequestType from a dict
query_v_motion_compatibility_ex_request_type_form_dict = query_v_motion_compatibility_ex_request_type.from_dict(query_v_motion_compatibility_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


