# ArrayOfVirtualMachineVideoCard

A boxed array of *VirtualMachineVideoCard*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVideoCard]**](VirtualMachineVideoCard.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_video_card import ArrayOfVirtualMachineVideoCard

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVideoCard from a JSON string
array_of_virtual_machine_video_card_instance = ArrayOfVirtualMachineVideoCard.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVideoCard.to_json()

# convert the object into a dict
array_of_virtual_machine_video_card_dict = array_of_virtual_machine_video_card_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVideoCard from a dict
array_of_virtual_machine_video_card_form_dict = array_of_virtual_machine_video_card.from_dict(array_of_virtual_machine_video_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


