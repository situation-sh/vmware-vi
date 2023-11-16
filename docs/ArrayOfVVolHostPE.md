# ArrayOfVVolHostPE

A boxed array of *VVolHostPE*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VVolHostPE]**](VVolHostPE.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_vol_host_pe import ArrayOfVVolHostPE

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVVolHostPE from a JSON string
array_of_v_vol_host_pe_instance = ArrayOfVVolHostPE.from_json(json)
# print the JSON string representation of the object
print ArrayOfVVolHostPE.to_json()

# convert the object into a dict
array_of_v_vol_host_pe_dict = array_of_v_vol_host_pe_instance.to_dict()
# create an instance of ArrayOfVVolHostPE from a dict
array_of_v_vol_host_pe_form_dict = array_of_v_vol_host_pe.from_dict(array_of_v_vol_host_pe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


