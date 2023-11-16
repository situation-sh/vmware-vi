# SelectVnicRequestType

The parameters of *HostVMotionSystem.SelectVnic*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device that uniquely identifies the VirtualNic.  | 

## Example

```python
from vmware_vi.models.select_vnic_request_type import SelectVnicRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SelectVnicRequestType from a JSON string
select_vnic_request_type_instance = SelectVnicRequestType.from_json(json)
# print the JSON string representation of the object
print SelectVnicRequestType.to_json()

# convert the object into a dict
select_vnic_request_type_dict = select_vnic_request_type_instance.to_dict()
# create an instance of SelectVnicRequestType from a dict
select_vnic_request_type_form_dict = select_vnic_request_type.from_dict(select_vnic_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


