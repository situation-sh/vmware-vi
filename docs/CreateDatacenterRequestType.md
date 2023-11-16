# CreateDatacenterRequestType

The parameters of *Folder.CreateDatacenter*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the new datacenter. An entity name must be a non-empty string of less than 80 characters. The slash (/), backslash (\\\\) and percent (%) will be escaped using the URL syntax. For example, %2F.  | 

## Example

```python
from vmware_vi.models.create_datacenter_request_type import CreateDatacenterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDatacenterRequestType from a JSON string
create_datacenter_request_type_instance = CreateDatacenterRequestType.from_json(json)
# print the JSON string representation of the object
print CreateDatacenterRequestType.to_json()

# convert the object into a dict
create_datacenter_request_type_dict = create_datacenter_request_type_instance.to_dict()
# create an instance of CreateDatacenterRequestType from a dict
create_datacenter_request_type_form_dict = create_datacenter_request_type.from_dict(create_datacenter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


