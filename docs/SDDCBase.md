# SDDCBase

An empty data object which can be used as the base class for data objects outside VIM namespace which have to be proxied through vCenter opaquely.  For example, vSan configuration spec will extend from this which will allow HCI API to pass the spec to set up vSan on the cluster.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.sddc_base import SDDCBase

# TODO update the JSON string below
json = "{}"
# create an instance of SDDCBase from a JSON string
sddc_base_instance = SDDCBase.from_json(json)
# print the JSON string representation of the object
print SDDCBase.to_json()

# convert the object into a dict
sddc_base_dict = sddc_base_instance.to_dict()
# create an instance of SDDCBase from a dict
sddc_base_form_dict = sddc_base.from_dict(sddc_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


