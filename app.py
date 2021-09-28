{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f72cdb9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import\n",
    "from flask import Flask, jsonify\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import sqlalchemy\n",
    "import datetime as dt\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6fef35db",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Engines and Database\n",
    "engine = create_engine(\"sqlite:///Resources/hawaii.sqlite\")\n",
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect = True)\n",
    "\n",
    "Station = Base.classes.station\n",
    "Measurement = Base.classes.measurement\n",
    "\n",
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2db27cdf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
