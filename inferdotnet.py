"""
Infer.Net IronPython wrapper

Sets up Infer.Net environment and creates convenience aliases to API modules
"""

import clr
import sys
import os

# add path to Infer.Net DLLs
sys.path.append(os.environ['INFERDOTNETPATH'])
clr.AddReferenceToFile('Infer.Compiler.dll')
clr.AddReferenceToFile('Infer.Runtime.dll')

# typed arrays for interop with .NET CLR
from System import Array

# add aliases to Infer.Net API modules
import MicrosoftResearch.Infer as Infer
import MicrosoftResearch.Infer.Models as Models
import MicrosoftResearch.Infer.Distributions as Distributions
import MicrosoftResearch.Infer.Collections as Collections
import MicrosoftResearch.Infer.Factors as Factors
import MicrosoftResearch.Infer.Maths as Maths
import MicrosoftResearch.Infer.Maths.Vector as Vector
import MicrosoftResearch.Infer.Models.Variable as Variable
