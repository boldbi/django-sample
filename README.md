# BoldBI Embedding Django Sample

This Bold BI Django sample repository contains the Dashboard embedding sample. This sample demonstrates how to embed the dashboard which is available in your Bold BI server.

This section guides you in using the Bold BI dashboard in your Django sample application.

* [Requirements to run the demo](#requirements-to-run-the-demo)
* [Using the Django sample](#using-the-django-sample)
* [Online Demos](#online-demos)
* [Documentation](#documentation)

## Requirements to run the demo

The samples require the following to run:

* [Python installer] (<https://www.python.org/downloads/>)
* [Visual Studio Code](https://code.visualstudio.com/download)
* [Python extension in VS code] (<https://marketplace.visualstudio.com/items?itemName=ms-python.python>)

## Using the Django sample

* Open the Django embed sample in Visual studio code or any respective IDE.

* Open the models.py file in the following location, /dashboardapp/models.py.

* Please change the following properties in the `models.py` file as per your Bold BI Server.

    | Parameter         | Description |
    |-------------------|-------------|
    | **RootUrl**       | Dashboard Server URL (e.g., <http://localhost:5000/bi>, <http://demo.boldbi.com/bi>). |
    | **SiteIdentifier**| For the Bold BI Enterprise edition, it should be like `site/site1`. For Bold BI Cloud, it should be an empty string. |
    | **Environment**   | Your Bold BI application environment. (If Cloud, you should use `cloud`, if Enterprise, you should use `onpremise`). |
    | **dashboardId**   | ID of the dashboard you want to embed. |
    | **UserEmail**     | UserEmail of the Admin in your Bold BI, which would be used to get the dashboard list. |
    | **EmbedSecret**   | Get your EmbedSecret key from the Embed tab by enabling the `Enable embed authentication` on the [Administration page](https://help.boldbi.com/embedded-bi/site-administration/embed-settings/?utm_source=github&utm_medium=backlinks). |

* Now run the Django sample.

Please refer to the [help documentation](https://help.boldbi.com/embedded-bi/javascript-based/samples/v3.3.40-or-later/other-platform-samples/#django-sample-to-embed-the-dashboard?utm_source=github&utm_medium=backlinks) to know how to run the sample.

## Online Demos

Look at the Bold BI Embedding sample to live demo [here](https://samples.boldbi.com/embed?utm_source=github&utm_medium=backlinks).

## Documentation

A complete Bold BI Embedding documentation can be found on the [Bold BI Embedding Help](https://help.boldbi.com/embedded-bi/javascript-based/?utm_source=github&utm_medium=backlinks).
