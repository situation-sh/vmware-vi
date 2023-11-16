# VAppProductInfo

Information that describes what product a vApp contains, for example, the software that is installed in the contained virtual machines.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | A unique key for the product section  ***Since:*** vSphere API 4.0  | 
**class_id** | **str** | Class name for this attribute.  Valid values for classId: Any string except any white-space characters.  ***Since:*** vSphere API 4.0  | [optional] 
**instance_id** | **str** | Class name for this attribute.  Valid values for instanceId: Any string except any white-space characters.  ***Since:*** vSphere API 4.0  | [optional] 
**name** | **str** | Name of the product.  ***Since:*** vSphere API 4.0  | [optional] 
**vendor** | **str** | Vendor of the product.  ***Since:*** vSphere API 4.0  | [optional] 
**version** | **str** | Short version of the product, for example, 1.0.  ***Since:*** vSphere API 4.0  | [optional] 
**full_version** | **str** | Full-version of the product, for example, 1.0-build 12323.  ***Since:*** vSphere API 4.0  | [optional] 
**vendor_url** | **str** | URL to vendor homepage.  ***Since:*** vSphere API 4.0  | [optional] 
**product_url** | **str** | URL to product homepage.  ***Since:*** vSphere API 4.0  | [optional] 
**app_url** | **str** | URL to entry-point for application.  This is often specified using a macro, for example, http://${app.ip}/, where app.ip is a defined property on the virtual machine or vApp container.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.v_app_product_info import VAppProductInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VAppProductInfo from a JSON string
v_app_product_info_instance = VAppProductInfo.from_json(json)
# print the JSON string representation of the object
print VAppProductInfo.to_json()

# convert the object into a dict
v_app_product_info_dict = v_app_product_info_instance.to_dict()
# create an instance of VAppProductInfo from a dict
v_app_product_info_form_dict = v_app_product_info.from_dict(v_app_product_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


