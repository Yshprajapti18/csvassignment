from django.shortcuts import render
from .forms import DocumentForm
import pandas as pd
# Create your views here.

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['csv']
            summaryfile = file(uploaded_file)
            return render(request, 'summary.html', {
              'data' : summaryfile
            })
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {"form": form})

def file(doc):
    if(doc.name.endswith('.csv')):
        df = pd.read_csv(doc)
        summarydata = summary(df)
        return summarydata.to_dict(orient='records')
    else:
        df = pd.read_excel(doc)
        summarydata = summary(df)
        return summarydata.to_dict(orient='records')
    
def summary(df):
    summary_column = ['Cust State','DPD']
    df = df[summary_column]
    
    summary_df = df.groupby(summary_column).size().reset_index(name='count')
    return summary_df