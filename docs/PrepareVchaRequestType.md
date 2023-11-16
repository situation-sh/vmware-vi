# PrepareVchaRequestType

The parameters of *FailoverClusterConfigurator.prepareVcha_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_spec** | [**VchaClusterNetworkSpec**](VchaClusterNetworkSpec.md) |  | 

## Example

```python
from vmware_vi.models.prepare_vcha_request_type import PrepareVchaRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PrepareVchaRequestType from a JSON string
prepare_vcha_request_type_instance = PrepareVchaRequestType.from_json(json)
# print the JSON string representation of the object
print PrepareVchaRequestType.to_json()

# convert the object into a dict
prepare_vcha_request_type_dict = prepare_vcha_request_type_instance.to_dict()
# create an instance of PrepareVchaRequestType from a dict
prepare_vcha_request_type_form_dict = prepare_vcha_request_type.from_dict(prepare_vcha_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


