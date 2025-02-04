{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "24f716ef-7aac-425e-8e98-831434c6c423",
   "metadata": {},
   "source": [
    "## .copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "32326c8e-b7f2-435d-a70e-1c9316a7831e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python_copy\n",
      "python_copy\n",
      "tython_coty\n",
      "python_copy\n"
     ]
    }
   ],
   "source": [
    "x = 'python_copy'\n",
    "print(x)\n",
    "y = x\n",
    "print(y)\n",
    "y = y.replace('p','t')\n",
    "print(y)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "82f2f899-7b70-4742-a4b2-02e733032441",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['p', 'y', 't', 'h', 'o', 'n', '_', 'c', 'o', 'p', 'y']\n",
      "['p', 'y', 't', 'h', 'o', 'n', '_', 'c', 'o', 'p', 'y']\n",
      "ls1: ['p', 'y', 't', 'h', 'o', 'n', '_', 'c', 'o', 'p', 'y', '99']\n",
      "ls2: ['p', 'y', 't', 'h', 'o', 'n', '_', 'c', 'o', 'p', 'y', '99']\n"
     ]
    }
   ],
   "source": [
    "ls1 = list(x)\n",
    "ls2 = ls1\n",
    "print(ls1)\n",
    "print(ls2)\n",
    "ls2.append('99')\n",
    "print('ls1:', ls1)\n",
    "print('ls2:', ls2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f0a533ee-5816-4b7d-b1f0-c6ff74612097",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "data = pd.read_csv('Lending-company.csv', index_col = 'LoanID')\n",
    "lending_co_data = data.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f16df965-aa9d-44bd-91f4-7b9b6b8f3738",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sr.no</th>\n",
       "      <th>Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Aslam</td>\n",
       "      <td>male</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Sara</td>\n",
       "      <td>female</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Ahmad</td>\n",
       "      <td>male</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Amna</td>\n",
       "      <td>female</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sr.no   Name  Gender  Age\n",
       "0      1  Aslam    male   22\n",
       "1      2   Sara  female   38\n",
       "2      3  Ahmad    male   26\n",
       "3      4   Amna  female   35"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''\n",
    "Sr.no,Name,Gender,Age\n",
    "1,\"Aslam\",male,22\n",
    "2,\"Sara\",female,38\n",
    "3,\"Ahmad\",male,26\n",
    "4,\"Amna\",female,35\n",
    "'''\n",
    "\n",
    "df = pd.read_csv('test.csv')\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "94b13386-fd13-43e3-bd8c-7e9c1e3ce394",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "# help(json.dump)\n",
    "df.to_json('test.json')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "c3593811-d1b9-4373-b5ac-daac12410232",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nSr.no,Name,Gender,Age\\n1,\"Aslam\",male,22\\n2,\"Sara\",female,38\\n3,\"Ahmad\",male,26\\n4,\"Amna\",female,35\\n'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = '''\n",
    "Sr.no,Name,Gender,Age\n",
    "1,\"Aslam\",male,22\n",
    "2,\"Sara\",female,38\n",
    "3,\"Ahmad\",male,26\n",
    "4,\"Amna\",female,35\n",
    "'''\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "3c659e11-665d-4509-a645-2e962575dcdf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Sr.no,Name,Gender,Age\n",
      "1,\"Aslam\",male,22\n",
      "2,\"Sara\",female,38\n",
      "3,\"Ahmad\",male,26\n",
      "4,\"Amna\",female,35\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "9d218c7e-76bd-4628-9af5-476d31cc70aa",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "OSError",
     "evalue": "[Errno 22] Invalid argument: '\\nSr.no,Name,Gender,Age\\n1,\"Aslam\",male,22\\n2,\"Sara\",female,38\\n3,\"Ahmad\",male,26\\n4,\"Amna\",female,35\\n'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[40], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m df \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(data)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1026\u001b[0m, in \u001b[0;36mread_csv\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)\u001b[0m\n\u001b[0;32m   1013\u001b[0m kwds_defaults \u001b[38;5;241m=\u001b[39m _refine_defaults_read(\n\u001b[0;32m   1014\u001b[0m     dialect,\n\u001b[0;32m   1015\u001b[0m     delimiter,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   1022\u001b[0m     dtype_backend\u001b[38;5;241m=\u001b[39mdtype_backend,\n\u001b[0;32m   1023\u001b[0m )\n\u001b[0;32m   1024\u001b[0m kwds\u001b[38;5;241m.\u001b[39mupdate(kwds_defaults)\n\u001b[1;32m-> 1026\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m _read(filepath_or_buffer, kwds)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:620\u001b[0m, in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    617\u001b[0m _validate_names(kwds\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnames\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    619\u001b[0m \u001b[38;5;66;03m# Create the parser.\u001b[39;00m\n\u001b[1;32m--> 620\u001b[0m parser \u001b[38;5;241m=\u001b[39m TextFileReader(filepath_or_buffer, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwds)\n\u001b[0;32m    622\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m chunksize \u001b[38;5;129;01mor\u001b[39;00m iterator:\n\u001b[0;32m    623\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m parser\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1620\u001b[0m, in \u001b[0;36mTextFileReader.__init__\u001b[1;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[0;32m   1617\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m kwds[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[0;32m   1619\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles: IOHandles \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m-> 1620\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_engine \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_make_engine(f, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mengine)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1880\u001b[0m, in \u001b[0;36mTextFileReader._make_engine\u001b[1;34m(self, f, engine)\u001b[0m\n\u001b[0;32m   1878\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m mode:\n\u001b[0;32m   1879\u001b[0m         mode \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1880\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;241m=\u001b[39m get_handle(\n\u001b[0;32m   1881\u001b[0m     f,\n\u001b[0;32m   1882\u001b[0m     mode,\n\u001b[0;32m   1883\u001b[0m     encoding\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mencoding\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[0;32m   1884\u001b[0m     compression\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcompression\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[0;32m   1885\u001b[0m     memory_map\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmemory_map\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mFalse\u001b[39;00m),\n\u001b[0;32m   1886\u001b[0m     is_text\u001b[38;5;241m=\u001b[39mis_text,\n\u001b[0;32m   1887\u001b[0m     errors\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mencoding_errors\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstrict\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[0;32m   1888\u001b[0m     storage_options\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstorage_options\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[0;32m   1889\u001b[0m )\n\u001b[0;32m   1890\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1891\u001b[0m f \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles\u001b[38;5;241m.\u001b[39mhandle\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\common.py:873\u001b[0m, in \u001b[0;36mget_handle\u001b[1;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[0;32m    868\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(handle, \u001b[38;5;28mstr\u001b[39m):\n\u001b[0;32m    869\u001b[0m     \u001b[38;5;66;03m# Check whether the filename is to be opened in binary mode.\u001b[39;00m\n\u001b[0;32m    870\u001b[0m     \u001b[38;5;66;03m# Binary mode does not support 'encoding' and 'newline'.\u001b[39;00m\n\u001b[0;32m    871\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mencoding \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mmode:\n\u001b[0;32m    872\u001b[0m         \u001b[38;5;66;03m# Encoding\u001b[39;00m\n\u001b[1;32m--> 873\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(\n\u001b[0;32m    874\u001b[0m             handle,\n\u001b[0;32m    875\u001b[0m             ioargs\u001b[38;5;241m.\u001b[39mmode,\n\u001b[0;32m    876\u001b[0m             encoding\u001b[38;5;241m=\u001b[39mioargs\u001b[38;5;241m.\u001b[39mencoding,\n\u001b[0;32m    877\u001b[0m             errors\u001b[38;5;241m=\u001b[39merrors,\n\u001b[0;32m    878\u001b[0m             newline\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    879\u001b[0m         )\n\u001b[0;32m    880\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    881\u001b[0m         \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n\u001b[0;32m    882\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(handle, ioargs\u001b[38;5;241m.\u001b[39mmode)\n",
      "\u001b[1;31mOSError\u001b[0m: [Errno 22] Invalid argument: '\\nSr.no,Name,Gender,Age\\n1,\"Aslam\",male,22\\n2,\"Sara\",female,38\\n3,\"Ahmad\",male,26\\n4,\"Amna\",female,35\\n'"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "a7da8f6d-fc3f-4581-ad17-8fe288a1c5dc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sr.no</th>\n",
       "      <th>Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Aslam</td>\n",
       "      <td>male</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Sara</td>\n",
       "      <td>female</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Ahmad</td>\n",
       "      <td>male</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Amna</td>\n",
       "      <td>female</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sr.no   Name  Gender  Age\n",
       "0      1  Aslam    male   22\n",
       "1      2   Sara  female   38\n",
       "2      3  Ahmad    male   26\n",
       "3      4   Amna  female   35"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from io import StringIO\n",
    "obj = StringIO(data)\n",
    "pd.read_csv(obj)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4eda7197-9cb2-4c18-bbfb-a7c841bcf3aa",
   "metadata": {},
   "source": [
    "## Handling Missing Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "2836c65c-3009-40a4-9d3d-f70fce957c81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "nan"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from numpy import nan\n",
    "nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "b7e03ecc-2c8f-4b65-b217-4a738e14f4ab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sr.no</th>\n",
       "      <th>Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>male</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Sara</td>\n",
       "      <td>NaN</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Ahmad</td>\n",
       "      <td>male</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Amna</td>\n",
       "      <td>female</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sr.no   Name  Gender  Age\n",
       "0      1    NaN    male   22\n",
       "1      2   Sara     NaN   38\n",
       "2      3  Ahmad    male   26\n",
       "3      4   Amna  female   35"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = '''\n",
    "Sr.no,Name,Gender,Age\n",
    "1,\"NA\",male,22\n",
    "2,\"Sara\",NA,38\n",
    "3,\"Ahmad\",male,26\n",
    "4,\"Amna\",female,35\n",
    "'''\n",
    "\n",
    "obj = StringIO(data)\n",
    "df = pd.read_csv(obj)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "366b2dd4-f18d-45aa-874a-a340b1433951",
   "metadata": {},
   "outputs": [],
   "source": [
    "sentinels = {'Gender':['male', 'NA']}\n",
    "df = pd.read_csv('test.csv', na_values=sentinels)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "ea4983da-17b3-4c53-b781-fbb1e8bb5f9d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sr.no</th>\n",
       "      <th>Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Aslam</td>\n",
       "      <td>NaN</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Sara</td>\n",
       "      <td>female</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Ahmad</td>\n",
       "      <td>NaN</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Amna</td>\n",
       "      <td>female</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sr.no   Name  Gender  Age\n",
       "0      1  Aslam     NaN   22\n",
       "1      2   Sara  female   38\n",
       "2      3  Ahmad     NaN   26\n",
       "3      4   Amna  female   35"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "8c55b6bf-cf62-48df-a30d-cb8d4495106b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sr.no</th>\n",
       "      <th>Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Sara</td>\n",
       "      <td>female</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Amna</td>\n",
       "      <td>female</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sr.no  Name  Gender  Age\n",
       "1      2  Sara  female   38\n",
       "3      4  Amna  female   35"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dropna(how='any')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "5726f2af-6c7b-4730-95bc-6043628fe799",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sr.no</th>\n",
       "      <th>Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Aslam</td>\n",
       "      <td>NaN</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Sara</td>\n",
       "      <td>female</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Ahmad</td>\n",
       "      <td>NaN</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Amna</td>\n",
       "      <td>female</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sr.no   Name  Gender  Age\n",
       "0      1  Aslam     NaN   22\n",
       "1      2   Sara  female   38\n",
       "2      3  Ahmad     NaN   26\n",
       "3      4   Amna  female   35"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dropna(how='all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "aa403d85-ebd6-40a1-b0be-5b8320d923a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sr.no</th>\n",
       "      <th>Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Aslam</td>\n",
       "      <td>M</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Sara</td>\n",
       "      <td>female</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Ahmad</td>\n",
       "      <td>M</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Amna</td>\n",
       "      <td>female</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sr.no   Name  Gender  Age\n",
       "0      1  Aslam       M   22\n",
       "1      2   Sara  female   38\n",
       "2      3  Ahmad       M   26\n",
       "3      4   Amna  female   35"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.fillna('M')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "8cc832b8-208a-47b4-8c07-173da4ef64a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sr.no</th>\n",
       "      <th>Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Aslam</td>\n",
       "      <td>male</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Sara</td>\n",
       "      <td>female</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Ahmad</td>\n",
       "      <td>male</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Amna</td>\n",
       "      <td>female</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sr.no   Name  Gender  Age\n",
       "0      1  Aslam    male   22\n",
       "1      2   Sara  female   38\n",
       "2      3  Ahmad    male   26\n",
       "3      4   Amna  female   35"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.read_json('test.json')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "79a586be-59bf-48fb-b22a-c5b4ff7bd062",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {\"Sr.no\":{\"0\":1,\"1\":2,\"2\":3,\"3\":4},\"Name\":{\"0\":\"Aslam\",\"1\":\"Sara\",\"2\":\"Ahmad\",\"3\":\"Amna\"},\"Gender\":{\"0\":\"male\",\"1\":\"female\",\"2\":\"male\",\"3\":\"female\"},\"Age\":{\"0\":22,\"1\":38,\"2\":26,\"3\":35}}\n",
    "df1 = pd.DataFrame(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "2baa0c45-ac7e-49b9-b1cd-dcbe8a594df2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sr.no</th>\n",
       "      <th>Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Aslam</td>\n",
       "      <td>male</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Sara</td>\n",
       "      <td>female</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Ahmad</td>\n",
       "      <td>male</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Amna</td>\n",
       "      <td>female</td>\n",
       "      <td>35</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sr.no   Name  Gender  Age\n",
       "0      1  Aslam    male   22\n",
       "1      2   Sara  female   38\n",
       "2      3  Ahmad    male   26\n",
       "3      4   Amna  female   35"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "0e3cb69b-cf4c-4260-807e-29051883b3d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TotalPrice</th>\n",
       "      <th>Deposit</th>\n",
       "      <th>DailyRate</th>\n",
       "      <th>TotalDaysYr</th>\n",
       "      <th>AmtPaid36</th>\n",
       "      <th>AmtPaid60</th>\n",
       "      <th>AmtPaid360</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1018.000000</td>\n",
       "      <td>1043.000000</td>\n",
       "      <td>1043.000000</td>\n",
       "      <td>1043.0</td>\n",
       "      <td>1043.000000</td>\n",
       "      <td>1043.000000</td>\n",
       "      <td>1043.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>19562.843811</td>\n",
       "      <td>2528.092042</td>\n",
       "      <td>50.834132</td>\n",
       "      <td>365.0</td>\n",
       "      <td>3901.857143</td>\n",
       "      <td>5214.393097</td>\n",
       "      <td>17122.131352</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>5955.588065</td>\n",
       "      <td>1504.467724</td>\n",
       "      <td>11.567390</td>\n",
       "      <td>0.0</td>\n",
       "      <td>2537.597667</td>\n",
       "      <td>2850.327133</td>\n",
       "      <td>5910.916736</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>13475.000000</td>\n",
       "      <td>1000.000000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>365.0</td>\n",
       "      <td>-2770.000000</td>\n",
       "      <td>-2945.000000</td>\n",
       "      <td>650.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>16300.000000</td>\n",
       "      <td>2200.000000</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>365.0</td>\n",
       "      <td>2840.500000</td>\n",
       "      <td>3822.000000</td>\n",
       "      <td>15560.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>17600.000000</td>\n",
       "      <td>2200.000000</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>365.0</td>\n",
       "      <td>3420.000000</td>\n",
       "      <td>4742.000000</td>\n",
       "      <td>16617.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>20950.000000</td>\n",
       "      <td>2200.000000</td>\n",
       "      <td>55.000000</td>\n",
       "      <td>365.0</td>\n",
       "      <td>5075.500000</td>\n",
       "      <td>6393.000000</td>\n",
       "      <td>19977.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>70225.000000</td>\n",
       "      <td>8000.000000</td>\n",
       "      <td>150.000000</td>\n",
       "      <td>365.0</td>\n",
       "      <td>18851.000000</td>\n",
       "      <td>22143.000000</td>\n",
       "      <td>65001.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         TotalPrice      Deposit    DailyRate  TotalDaysYr     AmtPaid36  \\\n",
       "count   1018.000000  1043.000000  1043.000000       1043.0   1043.000000   \n",
       "mean   19562.843811  2528.092042    50.834132        365.0   3901.857143   \n",
       "std     5955.588065  1504.467724    11.567390          0.0   2537.597667   \n",
       "min    13475.000000  1000.000000    30.000000        365.0  -2770.000000   \n",
       "25%    16300.000000  2200.000000    45.000000        365.0   2840.500000   \n",
       "50%    17600.000000  2200.000000    45.000000        365.0   3420.000000   \n",
       "75%    20950.000000  2200.000000    55.000000        365.0   5075.500000   \n",
       "max    70225.000000  8000.000000   150.000000        365.0  18851.000000   \n",
       "\n",
       "          AmtPaid60    AmtPaid360  \n",
       "count   1043.000000   1043.000000  \n",
       "mean    5214.393097  17122.131352  \n",
       "std     2850.327133   5910.916736  \n",
       "min    -2945.000000    650.000000  \n",
       "25%     3822.000000  15560.500000  \n",
       "50%     4742.000000  16617.000000  \n",
       "75%     6393.000000  19977.500000  \n",
       "max    22143.000000  65001.000000  "
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lending_co_data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "57a9ea9d-ab74-4147-beb6-9eb4701f43f6",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>StringID</th>\n",
       "      <th>Product</th>\n",
       "      <th>CustomerGender</th>\n",
       "      <th>Location</th>\n",
       "      <th>Region</th>\n",
       "      <th>TotalPrice</th>\n",
       "      <th>StartDate</th>\n",
       "      <th>Deposit</th>\n",
       "      <th>DailyRate</th>\n",
       "      <th>TotalDaysYr</th>\n",
       "      <th>AmtPaid36</th>\n",
       "      <th>AmtPaid60</th>\n",
       "      <th>AmtPaid360</th>\n",
       "      <th>LoanStatus</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>LoanID</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>LoanID_1</td>\n",
       "      <td>Product B</td>\n",
       "      <td>Female</td>\n",
       "      <td>Location 3</td>\n",
       "      <td>Region 2</td>\n",
       "      <td>17600.0</td>\n",
       "      <td>04/07/2018</td>\n",
       "      <td>2200</td>\n",
       "      <td>45</td>\n",
       "      <td>365</td>\n",
       "      <td>3221</td>\n",
       "      <td>4166</td>\n",
       "      <td>14621</td>\n",
       "      <td>Active</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>LoanID_2</td>\n",
       "      <td>Product D</td>\n",
       "      <td>Female</td>\n",
       "      <td>Location 6</td>\n",
       "      <td>Region 6</td>\n",
       "      <td>NaN</td>\n",
       "      <td>02/01/2019</td>\n",
       "      <td>2200</td>\n",
       "      <td>45</td>\n",
       "      <td>365</td>\n",
       "      <td>3161</td>\n",
       "      <td>4096</td>\n",
       "      <td>16041</td>\n",
       "      <td>Active</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>LoanID_3</td>\n",
       "      <td>Product B</td>\n",
       "      <td>Male</td>\n",
       "      <td>Location 8</td>\n",
       "      <td>Region 3</td>\n",
       "      <td>16600.0</td>\n",
       "      <td>08/12/2016</td>\n",
       "      <td>1000</td>\n",
       "      <td>45</td>\n",
       "      <td>365</td>\n",
       "      <td>2260</td>\n",
       "      <td>3205</td>\n",
       "      <td>16340</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>LoanID_4</td>\n",
       "      <td>Product A</td>\n",
       "      <td>Male</td>\n",
       "      <td>Location 26</td>\n",
       "      <td>Region 2</td>\n",
       "      <td>17600.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2200</td>\n",
       "      <td>45</td>\n",
       "      <td>365</td>\n",
       "      <td>3141</td>\n",
       "      <td>4166</td>\n",
       "      <td>16321</td>\n",
       "      <td>Active</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>LoanID_5</td>\n",
       "      <td>Product B</td>\n",
       "      <td>Female</td>\n",
       "      <td>Location 34</td>\n",
       "      <td>Region 3</td>\n",
       "      <td>21250.0</td>\n",
       "      <td>28/10/2017</td>\n",
       "      <td>2200</td>\n",
       "      <td>55</td>\n",
       "      <td>365</td>\n",
       "      <td>3570</td>\n",
       "      <td>4745</td>\n",
       "      <td>14720</td>\n",
       "      <td>Active</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1039</th>\n",
       "      <td>LoanID_1039</td>\n",
       "      <td>Product B</td>\n",
       "      <td>Male</td>\n",
       "      <td>Location 73</td>\n",
       "      <td>Region 6</td>\n",
       "      <td>17300.0</td>\n",
       "      <td>29/12/2018</td>\n",
       "      <td>2200</td>\n",
       "      <td>45</td>\n",
       "      <td>365</td>\n",
       "      <td>3251</td>\n",
       "      <td>4743</td>\n",
       "      <td>16617</td>\n",
       "      <td>Finished Payment</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1040</th>\n",
       "      <td>LoanID_1040</td>\n",
       "      <td>Product A</td>\n",
       "      <td>Male</td>\n",
       "      <td>Location 82</td>\n",
       "      <td>Region 1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>28/03/2018</td>\n",
       "      <td>2200</td>\n",
       "      <td>45</td>\n",
       "      <td>365</td>\n",
       "      <td>4090</td>\n",
       "      <td>5582</td>\n",
       "      <td>16617</td>\n",
       "      <td>Finished Payment</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1041</th>\n",
       "      <td>LoanID_1041</td>\n",
       "      <td>Product A</td>\n",
       "      <td>NotSpecified</td>\n",
       "      <td>Location 11</td>\n",
       "      <td>Region 4</td>\n",
       "      <td>17300.0</td>\n",
       "      <td>26/04/2018</td>\n",
       "      <td>2200</td>\n",
       "      <td>45</td>\n",
       "      <td>365</td>\n",
       "      <td>4051</td>\n",
       "      <td>5143</td>\n",
       "      <td>16617</td>\n",
       "      <td>Finished Payment</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1042</th>\n",
       "      <td>LoanID_1042</td>\n",
       "      <td>Product B</td>\n",
       "      <td>Female</td>\n",
       "      <td>Location 26</td>\n",
       "      <td>Region 6</td>\n",
       "      <td>16300.0</td>\n",
       "      <td>25/10/2016</td>\n",
       "      <td>1000</td>\n",
       "      <td>45</td>\n",
       "      <td>365</td>\n",
       "      <td>1930</td>\n",
       "      <td>3462</td>\n",
       "      <td>15617</td>\n",
       "      <td>Finished Payment</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1043</th>\n",
       "      <td>LoanID_1043</td>\n",
       "      <td>Product A</td>\n",
       "      <td>NotSpecified</td>\n",
       "      <td>Location 94</td>\n",
       "      <td>Region 6</td>\n",
       "      <td>17300.0</td>\n",
       "      <td>15/05/2019</td>\n",
       "      <td>2200</td>\n",
       "      <td>45</td>\n",
       "      <td>365</td>\n",
       "      <td>4451</td>\n",
       "      <td>4743</td>\n",
       "      <td>16617</td>\n",
       "      <td>Finished Payment</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1043 rows × 14 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           StringID    Product CustomerGender     Location    Region  \\\n",
       "LoanID                                                                 \n",
       "1          LoanID_1  Product B         Female   Location 3  Region 2   \n",
       "2          LoanID_2  Product D         Female   Location 6  Region 6   \n",
       "3          LoanID_3  Product B           Male   Location 8  Region 3   \n",
       "4          LoanID_4  Product A           Male  Location 26  Region 2   \n",
       "5          LoanID_5  Product B         Female  Location 34  Region 3   \n",
       "...             ...        ...            ...          ...       ...   \n",
       "1039    LoanID_1039  Product B           Male  Location 73  Region 6   \n",
       "1040    LoanID_1040  Product A           Male  Location 82  Region 1   \n",
       "1041    LoanID_1041  Product A   NotSpecified  Location 11  Region 4   \n",
       "1042    LoanID_1042  Product B         Female  Location 26  Region 6   \n",
       "1043    LoanID_1043  Product A   NotSpecified  Location 94  Region 6   \n",
       "\n",
       "        TotalPrice   StartDate  Deposit  DailyRate  TotalDaysYr  AmtPaid36  \\\n",
       "LoanID                                                                       \n",
       "1          17600.0  04/07/2018     2200         45          365       3221   \n",
       "2              NaN  02/01/2019     2200         45          365       3161   \n",
       "3          16600.0  08/12/2016     1000         45          365       2260   \n",
       "4          17600.0         NaN     2200         45          365       3141   \n",
       "5          21250.0  28/10/2017     2200         55          365       3570   \n",
       "...            ...         ...      ...        ...          ...        ...   \n",
       "1039       17300.0  29/12/2018     2200         45          365       3251   \n",
       "1040           NaN  28/03/2018     2200         45          365       4090   \n",
       "1041       17300.0  26/04/2018     2200         45          365       4051   \n",
       "1042       16300.0  25/10/2016     1000         45          365       1930   \n",
       "1043       17300.0  15/05/2019     2200         45          365       4451   \n",
       "\n",
       "        AmtPaid60  AmtPaid360        LoanStatus  \n",
       "LoanID                                           \n",
       "1            4166       14621            Active  \n",
       "2            4096       16041            Active  \n",
       "3            3205       16340               NaN  \n",
       "4            4166       16321            Active  \n",
       "5            4745       14720            Active  \n",
       "...           ...         ...               ...  \n",
       "1039         4743       16617  Finished Payment  \n",
       "1040         5582       16617  Finished Payment  \n",
       "1041         5143       16617  Finished Payment  \n",
       "1042         3462       15617  Finished Payment  \n",
       "1043         4743       16617  Finished Payment  \n",
       "\n",
       "[1043 rows x 14 columns]"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lending_co_data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e8b01dd-ed3c-41b3-b8b5-70386693ba2c",
   "metadata": {},
   "source": [
    "## unique and nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "557448e3-0cfe-4793-8b67-5fcbdedc6277",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "StringID          1043\n",
       "Product              6\n",
       "CustomerGender       3\n",
       "Location           296\n",
       "Region              18\n",
       "TotalPrice          24\n",
       "StartDate          742\n",
       "Deposit              5\n",
       "DailyRate            5\n",
       "TotalDaysYr          1\n",
       "AmtPaid36          455\n",
       "AmtPaid60          612\n",
       "AmtPaid360         458\n",
       "LoanStatus           3\n",
       "dtype: int64"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lending_co_data.nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "14459cce-04ab-43be-a288-614ac0b0bb97",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.series.Series"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(lending_co_data['Deposit'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "69527004-f951-4dea-8000-306ac265d182",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2200, 1000, 5000, 3000, 8000], dtype=int64)"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lending_co_data['Deposit'].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b5a19192-dca6-4779-9d75-e0e51a68e574",
   "metadata": {},
   "source": [
    "## Modifying"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "25cb5d94-1342-4ff3-98b5-a0ca2e78ebdf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>c</td>\n",
       "      <td>d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>e</td>\n",
       "      <td>f</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>g</td>\n",
       "      <td>h</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  col1 col2\n",
       "0    a    b\n",
       "1    c    d\n",
       "2    e    f\n",
       "3    g    h"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame([['a','b'], ['c', 'd'], ['e', 'f'], ['g', 'h']], columns=['col1','col2'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "d2caa796-d358-4e47-88be-9ef765566e9d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>c</td>\n",
       "      <td>d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>e</td>\n",
       "      <td>x</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>g</td>\n",
       "      <td>y</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  col1 col2\n",
       "0    a    b\n",
       "1    c    d\n",
       "2    e    x\n",
       "3    g    y"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[2:4,1] = ['x','y']\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "0eb4ac64-c9bd-466a-bca0-e93b61fbb513",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>c</td>\n",
       "      <td>d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>e</td>\n",
       "      <td>x</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>g</td>\n",
       "      <td>x</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  col1 col2\n",
       "0    a    b\n",
       "1    c    d\n",
       "2    e    x\n",
       "3    g    x"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[2:4,1] = ['x']\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "45d64913-6224-4633-9065-0267a1b43167",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  col1 col2\n",
      "0    a    b\n",
      "1    c    d\n",
      "2    e    x\n",
      "3    g    x\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "1f13f337-84eb-4d13-94bb-28f07b5720c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.rename(index={2:'r2', 3:'r3'})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "1c4b255e-b014-41d6-9fca-c453a70df5b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>c</td>\n",
       "      <td>d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>r2</th>\n",
       "      <td>e</td>\n",
       "      <td>x</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>r3</th>\n",
       "      <td>g</td>\n",
       "      <td>x</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   col1 col2\n",
       "0     a    b\n",
       "1     c    d\n",
       "r2    e    x\n",
       "r3    g    x"
      ]
     },
     "execution_count": 121,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "75020a60-f708-4ea4-a0b1-df77313709dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "col1    e\n",
       "col2    x\n",
       "Name: r2, dtype: object"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc['r2']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "98d99c48-b293-468c-a7b3-f8706f298610",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on method insert in module pandas.core.frame:\n",
      "\n",
      "insert(loc: 'int', column: 'Hashable', value: 'Scalar | AnyArrayLike', allow_duplicates: 'bool | lib.NoDefault' = <no_default>) -> 'None' method of pandas.core.frame.DataFrame instance\n",
      "    Insert column into DataFrame at specified location.\n",
      "\n",
      "    Raises a ValueError if `column` is already contained in the DataFrame,\n",
      "    unless `allow_duplicates` is set to True.\n",
      "\n",
      "    Parameters\n",
      "    ----------\n",
      "    loc : int\n",
      "        Insertion index. Must verify 0 <= loc <= len(columns).\n",
      "    column : str, number, or hashable object\n",
      "        Label of the inserted column.\n",
      "    value : Scalar, Series, or array-like\n",
      "        Content of the inserted column.\n",
      "    allow_duplicates : bool, optional, default lib.no_default\n",
      "        Allow duplicate column labels to be created.\n",
      "\n",
      "    See Also\n",
      "    --------\n",
      "    Index.insert : Insert new item by index.\n",
      "\n",
      "    Examples\n",
      "    --------\n",
      "    >>> df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})\n",
      "    >>> df\n",
      "       col1  col2\n",
      "    0     1     3\n",
      "    1     2     4\n",
      "    >>> df.insert(1, \"newcol\", [99, 99])\n",
      "    >>> df\n",
      "       col1  newcol  col2\n",
      "    0     1      99     3\n",
      "    1     2      99     4\n",
      "    >>> df.insert(0, \"col1\", [100, 100], allow_duplicates=True)\n",
      "    >>> df\n",
      "       col1  col1  newcol  col2\n",
      "    0   100     1      99     3\n",
      "    1   100     2      99     4\n",
      "\n",
      "    Notice that pandas uses index alignment in case of `value` from type `Series`:\n",
      "\n",
      "    >>> df.insert(0, \"col0\", pd.Series([5, 6], index=[1, 2]))\n",
      "    >>> df\n",
      "       col0  col1  col1  newcol  col2\n",
      "    0   NaN   100     1      99     3\n",
      "    1   5.0   100     2      99     4\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(df.insert)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "32c72348-eda3-48f5-994a-e3d3106f827b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.insert(2, 'col3', [99,99,99,99])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "ee33905d-feb3-434e-ae5d-530fe3a301be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "d760e341-25ee-4ad1-94e1-f66626575048",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>c</td>\n",
       "      <td>d</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>e</td>\n",
       "      <td>f</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>g</td>\n",
       "      <td>h</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  col1 col2\n",
       "0    a    b\n",
       "1    c    d\n",
       "2    e    f\n",
       "3    g    h"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame([['a','b'], ['c', 'd'], ['e', 'f'], ['g', 'h']], columns=['col1','col2'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "b9998ffd-6bd3-445a-a103-6f6660eda551",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "      <th>col3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>c</td>\n",
       "      <td>d</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>e</td>\n",
       "      <td>f</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>g</td>\n",
       "      <td>h</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  col1 col2  col3\n",
       "0    a    b    99\n",
       "1    c    d    99\n",
       "2    e    f    99\n",
       "3    g    h    99"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.insert(2, 'col3', [99,99,99,99])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "17a7b5da-42bc-4704-a40c-622b6d06e52b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on method drop in module pandas.core.frame:\n",
      "\n",
      "drop(labels: 'IndexLabel | None' = None, *, axis: 'Axis' = 0, index: 'IndexLabel | None' = None, columns: 'IndexLabel | None' = None, level: 'Level | None' = None, inplace: 'bool' = False, errors: 'IgnoreRaise' = 'raise') -> 'DataFrame | None' method of pandas.core.frame.DataFrame instance\n",
      "    Drop specified labels from rows or columns.\n",
      "\n",
      "    Remove rows or columns by specifying label names and corresponding\n",
      "    axis, or by directly specifying index or column names. When using a\n",
      "    multi-index, labels on different levels can be removed by specifying\n",
      "    the level. See the :ref:`user guide <advanced.shown_levels>`\n",
      "    for more information about the now unused levels.\n",
      "\n",
      "    Parameters\n",
      "    ----------\n",
      "    labels : single label or list-like\n",
      "        Index or column labels to drop. A tuple will be used as a single\n",
      "        label and not treated as a list-like.\n",
      "    axis : {0 or 'index', 1 or 'columns'}, default 0\n",
      "        Whether to drop labels from the index (0 or 'index') or\n",
      "        columns (1 or 'columns').\n",
      "    index : single label or list-like\n",
      "        Alternative to specifying axis (``labels, axis=0``\n",
      "        is equivalent to ``index=labels``).\n",
      "    columns : single label or list-like\n",
      "        Alternative to specifying axis (``labels, axis=1``\n",
      "        is equivalent to ``columns=labels``).\n",
      "    level : int or level name, optional\n",
      "        For MultiIndex, level from which the labels will be removed.\n",
      "    inplace : bool, default False\n",
      "        If False, return a copy. Otherwise, do operation\n",
      "        in place and return None.\n",
      "    errors : {'ignore', 'raise'}, default 'raise'\n",
      "        If 'ignore', suppress error and only existing labels are\n",
      "        dropped.\n",
      "\n",
      "    Returns\n",
      "    -------\n",
      "    DataFrame or None\n",
      "        Returns DataFrame or None DataFrame with the specified\n",
      "        index or column labels removed or None if inplace=True.\n",
      "\n",
      "    Raises\n",
      "    ------\n",
      "    KeyError\n",
      "        If any of the labels is not found in the selected axis.\n",
      "\n",
      "    See Also\n",
      "    --------\n",
      "    DataFrame.loc : Label-location based indexer for selection by label.\n",
      "    DataFrame.dropna : Return DataFrame with labels on given axis omitted\n",
      "        where (all or any) data are missing.\n",
      "    DataFrame.drop_duplicates : Return DataFrame with duplicate rows\n",
      "        removed, optionally only considering certain columns.\n",
      "    Series.drop : Return Series with specified index labels removed.\n",
      "\n",
      "    Examples\n",
      "    --------\n",
      "    >>> df = pd.DataFrame(np.arange(12).reshape(3, 4),\n",
      "    ...                   columns=['A', 'B', 'C', 'D'])\n",
      "    >>> df\n",
      "       A  B   C   D\n",
      "    0  0  1   2   3\n",
      "    1  4  5   6   7\n",
      "    2  8  9  10  11\n",
      "\n",
      "    Drop columns\n",
      "\n",
      "    >>> df.drop(['B', 'C'], axis=1)\n",
      "       A   D\n",
      "    0  0   3\n",
      "    1  4   7\n",
      "    2  8  11\n",
      "\n",
      "    >>> df.drop(columns=['B', 'C'])\n",
      "       A   D\n",
      "    0  0   3\n",
      "    1  4   7\n",
      "    2  8  11\n",
      "\n",
      "    Drop a row by index\n",
      "\n",
      "    >>> df.drop([0, 1])\n",
      "       A  B   C   D\n",
      "    2  8  9  10  11\n",
      "\n",
      "    Drop columns and/or rows of MultiIndex DataFrame\n",
      "\n",
      "    >>> midx = pd.MultiIndex(levels=[['llama', 'cow', 'falcon'],\n",
      "    ...                              ['speed', 'weight', 'length']],\n",
      "    ...                      codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2],\n",
      "    ...                             [0, 1, 2, 0, 1, 2, 0, 1, 2]])\n",
      "    >>> df = pd.DataFrame(index=midx, columns=['big', 'small'],\n",
      "    ...                   data=[[45, 30], [200, 100], [1.5, 1], [30, 20],\n",
      "    ...                         [250, 150], [1.5, 0.8], [320, 250],\n",
      "    ...                         [1, 0.8], [0.3, 0.2]])\n",
      "    >>> df\n",
      "                    big     small\n",
      "    llama   speed   45.0    30.0\n",
      "            weight  200.0   100.0\n",
      "            length  1.5     1.0\n",
      "    cow     speed   30.0    20.0\n",
      "            weight  250.0   150.0\n",
      "            length  1.5     0.8\n",
      "    falcon  speed   320.0   250.0\n",
      "            weight  1.0     0.8\n",
      "            length  0.3     0.2\n",
      "\n",
      "    Drop a specific index combination from the MultiIndex\n",
      "    DataFrame, i.e., drop the combination ``'falcon'`` and\n",
      "    ``'weight'``, which deletes only the corresponding row\n",
      "\n",
      "    >>> df.drop(index=('falcon', 'weight'))\n",
      "                    big     small\n",
      "    llama   speed   45.0    30.0\n",
      "            weight  200.0   100.0\n",
      "            length  1.5     1.0\n",
      "    cow     speed   30.0    20.0\n",
      "            weight  250.0   150.0\n",
      "            length  1.5     0.8\n",
      "    falcon  speed   320.0   250.0\n",
      "            length  0.3     0.2\n",
      "\n",
      "    >>> df.drop(index='cow', columns='small')\n",
      "                    big\n",
      "    llama   speed   45.0\n",
      "            weight  200.0\n",
      "            length  1.5\n",
      "    falcon  speed   320.0\n",
      "            weight  1.0\n",
      "            length  0.3\n",
      "\n",
      "    >>> df.drop(index='length', level=1)\n",
      "                    big     small\n",
      "    llama   speed   45.0    30.0\n",
      "            weight  200.0   100.0\n",
      "    cow     speed   30.0    20.0\n",
      "            weight  250.0   150.0\n",
      "    falcon  speed   320.0   250.0\n",
      "            weight  1.0     0.8\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(df.drop)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "b0d9cf15-cc0b-4fbb-89e9-211f7d222711",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "      <th>col3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>c</td>\n",
       "      <td>d</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>g</td>\n",
       "      <td>h</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  col1 col2  col3\n",
       "0    a    b    99\n",
       "1    c    d    99\n",
       "3    g    h    99"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "6dc1cf56-8a4c-47eb-9cb8-f88a8345b761",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "      <th>col3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>a</td>\n",
       "      <td>b</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>c</td>\n",
       "      <td>d</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>g</td>\n",
       "      <td>h</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  col1 col2  col3\n",
       "0    a    b    99\n",
       "1    c    d    99\n",
       "3    g    h    99"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop(2,inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "id": "716c099a-0e32-4b2a-875c-66fbfaca6bd5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col2</th>\n",
       "      <th>col3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>b</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>d</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>h</td>\n",
       "      <td>99</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  col2  col3\n",
       "0    b    99\n",
       "1    d    99\n",
       "3    h    99"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop(['col1'],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "745942a4-61ed-4243-92f8-6fdaabd56d88",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on method rename in module pandas.core.frame:\n",
      "\n",
      "rename(mapper: 'Renamer | None' = None, *, index: 'Renamer | None' = None, columns: 'Renamer | None' = None, axis: 'Axis | None' = None, copy: 'bool | None' = None, inplace: 'bool' = False, level: 'Level | None' = None, errors: 'IgnoreRaise' = 'ignore') -> 'DataFrame | None' method of pandas.core.frame.DataFrame instance\n",
      "    Rename columns or index labels.\n",
      "\n",
      "    Function / dict values must be unique (1-to-1). Labels not contained in\n",
      "    a dict / Series will be left as-is. Extra labels listed don't throw an\n",
      "    error.\n",
      "\n",
      "    See the :ref:`user guide <basics.rename>` for more.\n",
      "\n",
      "    Parameters\n",
      "    ----------\n",
      "    mapper : dict-like or function\n",
      "        Dict-like or function transformations to apply to\n",
      "        that axis' values. Use either ``mapper`` and ``axis`` to\n",
      "        specify the axis to target with ``mapper``, or ``index`` and\n",
      "        ``columns``.\n",
      "    index : dict-like or function\n",
      "        Alternative to specifying axis (``mapper, axis=0``\n",
      "        is equivalent to ``index=mapper``).\n",
      "    columns : dict-like or function\n",
      "        Alternative to specifying axis (``mapper, axis=1``\n",
      "        is equivalent to ``columns=mapper``).\n",
      "    axis : {0 or 'index', 1 or 'columns'}, default 0\n",
      "        Axis to target with ``mapper``. Can be either the axis name\n",
      "        ('index', 'columns') or number (0, 1). The default is 'index'.\n",
      "    copy : bool, default True\n",
      "        Also copy underlying data.\n",
      "\n",
      "        .. note::\n",
      "            The `copy` keyword will change behavior in pandas 3.0.\n",
      "            `Copy-on-Write\n",
      "            <https://pandas.pydata.org/docs/dev/user_guide/copy_on_write.html>`__\n",
      "            will be enabled by default, which means that all methods with a\n",
      "            `copy` keyword will use a lazy copy mechanism to defer the copy and\n",
      "            ignore the `copy` keyword. The `copy` keyword will be removed in a\n",
      "            future version of pandas.\n",
      "\n",
      "            You can already get the future behavior and improvements through\n",
      "            enabling copy on write ``pd.options.mode.copy_on_write = True``\n",
      "    inplace : bool, default False\n",
      "        Whether to modify the DataFrame rather than creating a new one.\n",
      "        If True then value of copy is ignored.\n",
      "    level : int or level name, default None\n",
      "        In case of a MultiIndex, only rename labels in the specified\n",
      "        level.\n",
      "    errors : {'ignore', 'raise'}, default 'ignore'\n",
      "        If 'raise', raise a `KeyError` when a dict-like `mapper`, `index`,\n",
      "        or `columns` contains labels that are not present in the Index\n",
      "        being transformed.\n",
      "        If 'ignore', existing keys will be renamed and extra keys will be\n",
      "        ignored.\n",
      "\n",
      "    Returns\n",
      "    -------\n",
      "    DataFrame or None\n",
      "        DataFrame with the renamed axis labels or None if ``inplace=True``.\n",
      "\n",
      "    Raises\n",
      "    ------\n",
      "    KeyError\n",
      "        If any of the labels is not found in the selected axis and\n",
      "        \"errors='raise'\".\n",
      "\n",
      "    See Also\n",
      "    --------\n",
      "    DataFrame.rename_axis : Set the name of the axis.\n",
      "\n",
      "    Examples\n",
      "    --------\n",
      "    ``DataFrame.rename`` supports two calling conventions\n",
      "\n",
      "    * ``(index=index_mapper, columns=columns_mapper, ...)``\n",
      "    * ``(mapper, axis={'index', 'columns'}, ...)``\n",
      "\n",
      "    We *highly* recommend using keyword arguments to clarify your\n",
      "    intent.\n",
      "\n",
      "    Rename columns using a mapping:\n",
      "\n",
      "    >>> df = pd.DataFrame({\"A\": [1, 2, 3], \"B\": [4, 5, 6]})\n",
      "    >>> df.rename(columns={\"A\": \"a\", \"B\": \"c\"})\n",
      "       a  c\n",
      "    0  1  4\n",
      "    1  2  5\n",
      "    2  3  6\n",
      "\n",
      "    Rename index using a mapping:\n",
      "\n",
      "    >>> df.rename(index={0: \"x\", 1: \"y\", 2: \"z\"})\n",
      "       A  B\n",
      "    x  1  4\n",
      "    y  2  5\n",
      "    z  3  6\n",
      "\n",
      "    Cast index labels to a different type:\n",
      "\n",
      "    >>> df.index\n",
      "    RangeIndex(start=0, stop=3, step=1)\n",
      "    >>> df.rename(index=str).index\n",
      "    Index(['0', '1', '2'], dtype='object')\n",
      "\n",
      "    >>> df.rename(columns={\"A\": \"a\", \"B\": \"b\", \"C\": \"c\"}, errors=\"raise\")\n",
      "    Traceback (most recent call last):\n",
      "    KeyError: ['C'] not found in axis\n",
      "\n",
      "    Using axis-style parameters:\n",
      "\n",
      "    >>> df.rename(str.lower, axis='columns')\n",
      "       a  b\n",
      "    0  1  4\n",
      "    1  2  5\n",
      "    2  3  6\n",
      "\n",
      "    >>> df.rename({1: 2, 2: 4}, axis='index')\n",
      "       A  B\n",
      "    0  1  4\n",
      "    2  2  5\n",
      "    4  3  6\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(df.rename)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3247a2fc-20ef-4ff8-ab63-e94429097880",
   "metadata": {},
   "source": [
    "## Filtering"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "14dfa73e-eb63-4dd4-8e84-e1f45b61c618",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   col1  col2\n",
       "0     1     2\n",
       "1     3     4\n",
       "2     5     6\n",
       "3     7     8"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame([[1,2], [3, 4], [5,6], [7,8]], columns=['col1','col2'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "9c87696f-fc9c-4ed7-8ffb-ee69d30fd682",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>col1</th>\n",
       "      <th>col2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    col1   col2\n",
       "0  False  False\n",
       "1  False   True\n",
       "2   True   True\n",
       "3   True   True"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df > 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "668f9610-2deb-4622-a1a3-fad477dee01b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2    6\n",
       "3    8\n",
       "Name: col2, dtype: int64"
      ]
     },
     "execution_count": 160,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "condition = (df['col1'] > 3)\n",
    "df.loc[condition,'col2']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "6944d246-142a-4b33-bf5d-23a2410a00e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    False\n",
       "1    False\n",
       "2     True\n",
       "3     True\n",
       "Name: col1, dtype: bool"
      ]
     },
     "execution_count": 166,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "condition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "efd7c19a-1e52-4c28-a8c4-78647faeffe9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.series.Series"
      ]
     },
     "execution_count": 164,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(condition)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "id": "a1f75abf-6299-4c4a-9801-894c78a06420",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>x</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>y</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5</td>\n",
       "      <td>8</td>\n",
       "      <td>x</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>7</td>\n",
       "      <td>4</td>\n",
       "      <td>z</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   A  B  C\n",
       "0  1  5  x\n",
       "1  3  2  y\n",
       "2  5  8  x\n",
       "3  7  4  z"
      ]
     },
     "execution_count": 170,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame({'A': [1,3,5,7], 'B': [5,2,8,4], 'C': ['x', 'y', 'x', 'z']})\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "id": "123b770a-47e3-4170-a196-36379051055f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2    x\n",
       "3    z\n",
       "Name: C, dtype: object"
      ]
     },
     "execution_count": 174,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[(df['A'] > 2) & (df['B'] > 2), 'C']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "id": "0c3a5ede-5b18-4d53-9ec2-27a923fc9567",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>8</td>\n",
       "      <td>x</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>z</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   B  C\n",
       "2  8  x\n",
       "3  4  z"
      ]
     },
     "execution_count": 176,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[(df['A'] > 2) & (df['B'] > 2), 'B':'C']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "fb6d1393-7cfe-44b2-a4f2-06f771181925",
   "metadata": {},
   "outputs": [],
   "source": [
    "mask = (df['A'] > 2) & (df['B'] > 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "68df0583-9006-4497-b31b-4c9de6f6641b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    False\n",
       "1    False\n",
       "2     True\n",
       "3     True\n",
       "dtype: bool"
      ]
     },
     "execution_count": 180,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "id": "556fe6ed-8dbc-4785-96a1-21c4b05dc600",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5</td>\n",
       "      <td>8</td>\n",
       "      <td>x</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>7</td>\n",
       "      <td>4</td>\n",
       "      <td>z</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   A  B  C\n",
       "2  5  8  x\n",
       "3  7  4  z"
      ]
     },
     "execution_count": 182,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[mask]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "id": "68ef968a-0a1c-4eac-8795-1b757a521375",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on method replace in module pandas.core.generic:\n",
      "\n",
      "replace(to_replace=None, value=<no_default>, *, inplace: 'bool_t' = False, limit: 'int | None' = None, regex: 'bool_t' = False, method: \"Literal['pad', 'ffill', 'bfill'] | lib.NoDefault\" = <no_default>) -> 'Self | None' method of pandas.core.frame.DataFrame instance\n",
      "    Replace values given in `to_replace` with `value`.\n",
      "\n",
      "    Values of the Series/DataFrame are replaced with other values dynamically.\n",
      "    This differs from updating with ``.loc`` or ``.iloc``, which require\n",
      "    you to specify a location to update with some value.\n",
      "\n",
      "    Parameters\n",
      "    ----------\n",
      "    to_replace : str, regex, list, dict, Series, int, float, or None\n",
      "        How to find the values that will be replaced.\n",
      "\n",
      "        * numeric, str or regex:\n",
      "\n",
      "            - numeric: numeric values equal to `to_replace` will be\n",
      "              replaced with `value`\n",
      "            - str: string exactly matching `to_replace` will be replaced\n",
      "              with `value`\n",
      "            - regex: regexs matching `to_replace` will be replaced with\n",
      "              `value`\n",
      "\n",
      "        * list of str, regex, or numeric:\n",
      "\n",
      "            - First, if `to_replace` and `value` are both lists, they\n",
      "              **must** be the same length.\n",
      "            - Second, if ``regex=True`` then all of the strings in **both**\n",
      "              lists will be interpreted as regexs otherwise they will match\n",
      "              directly. This doesn't matter much for `value` since there\n",
      "              are only a few possible substitution regexes you can use.\n",
      "            - str, regex and numeric rules apply as above.\n",
      "\n",
      "        * dict:\n",
      "\n",
      "            - Dicts can be used to specify different replacement values\n",
      "              for different existing values. For example,\n",
      "              ``{'a': 'b', 'y': 'z'}`` replaces the value 'a' with 'b' and\n",
      "              'y' with 'z'. To use a dict in this way, the optional `value`\n",
      "              parameter should not be given.\n",
      "            - For a DataFrame a dict can specify that different values\n",
      "              should be replaced in different columns. For example,\n",
      "              ``{'a': 1, 'b': 'z'}`` looks for the value 1 in column 'a'\n",
      "              and the value 'z' in column 'b' and replaces these values\n",
      "              with whatever is specified in `value`. The `value` parameter\n",
      "              should not be ``None`` in this case. You can treat this as a\n",
      "              special case of passing two lists except that you are\n",
      "              specifying the column to search in.\n",
      "            - For a DataFrame nested dictionaries, e.g.,\n",
      "              ``{'a': {'b': np.nan}}``, are read as follows: look in column\n",
      "              'a' for the value 'b' and replace it with NaN. The optional `value`\n",
      "              parameter should not be specified to use a nested dict in this\n",
      "              way. You can nest regular expressions as well. Note that\n",
      "              column names (the top-level dictionary keys in a nested\n",
      "              dictionary) **cannot** be regular expressions.\n",
      "\n",
      "        * None:\n",
      "\n",
      "            - This means that the `regex` argument must be a string,\n",
      "              compiled regular expression, or list, dict, ndarray or\n",
      "              Series of such elements. If `value` is also ``None`` then\n",
      "              this **must** be a nested dictionary or Series.\n",
      "\n",
      "        See the examples section for examples of each of these.\n",
      "    value : scalar, dict, list, str, regex, default None\n",
      "        Value to replace any values matching `to_replace` with.\n",
      "        For a DataFrame a dict of values can be used to specify which\n",
      "        value to use for each column (columns not in the dict will not be\n",
      "        filled). Regular expressions, strings and lists or dicts of such\n",
      "        objects are also allowed.\n",
      "\n",
      "    inplace : bool, default False\n",
      "        If True, performs operation inplace and returns None.\n",
      "    limit : int, default None\n",
      "        Maximum size gap to forward or backward fill.\n",
      "\n",
      "        .. deprecated:: 2.1.0\n",
      "    regex : bool or same types as `to_replace`, default False\n",
      "        Whether to interpret `to_replace` and/or `value` as regular\n",
      "        expressions. Alternatively, this could be a regular expression or a\n",
      "        list, dict, or array of regular expressions in which case\n",
      "        `to_replace` must be ``None``.\n",
      "    method : {'pad', 'ffill', 'bfill'}\n",
      "        The method to use when for replacement, when `to_replace` is a\n",
      "        scalar, list or tuple and `value` is ``None``.\n",
      "\n",
      "        .. deprecated:: 2.1.0\n",
      "\n",
      "    Returns\n",
      "    -------\n",
      "    Series/DataFrame\n",
      "        Object after replacement.\n",
      "\n",
      "    Raises\n",
      "    ------\n",
      "    AssertionError\n",
      "        * If `regex` is not a ``bool`` and `to_replace` is not\n",
      "          ``None``.\n",
      "\n",
      "    TypeError\n",
      "        * If `to_replace` is not a scalar, array-like, ``dict``, or ``None``\n",
      "        * If `to_replace` is a ``dict`` and `value` is not a ``list``,\n",
      "          ``dict``, ``ndarray``, or ``Series``\n",
      "        * If `to_replace` is ``None`` and `regex` is not compilable\n",
      "          into a regular expression or is a list, dict, ndarray, or\n",
      "          Series.\n",
      "        * When replacing multiple ``bool`` or ``datetime64`` objects and\n",
      "          the arguments to `to_replace` does not match the type of the\n",
      "          value being replaced\n",
      "\n",
      "    ValueError\n",
      "        * If a ``list`` or an ``ndarray`` is passed to `to_replace` and\n",
      "          `value` but they are not the same length.\n",
      "\n",
      "    See Also\n",
      "    --------\n",
      "    Series.fillna : Fill NA values.\n",
      "    DataFrame.fillna : Fill NA values.\n",
      "    Series.where : Replace values based on boolean condition.\n",
      "    DataFrame.where : Replace values based on boolean condition.\n",
      "    DataFrame.map: Apply a function to a Dataframe elementwise.\n",
      "    Series.map: Map values of Series according to an input mapping or function.\n",
      "    Series.str.replace : Simple string replacement.\n",
      "\n",
      "    Notes\n",
      "    -----\n",
      "    * Regex substitution is performed under the hood with ``re.sub``. The\n",
      "      rules for substitution for ``re.sub`` are the same.\n",
      "    * Regular expressions will only substitute on strings, meaning you\n",
      "      cannot provide, for example, a regular expression matching floating\n",
      "      point numbers and expect the columns in your frame that have a\n",
      "      numeric dtype to be matched. However, if those floating point\n",
      "      numbers *are* strings, then you can do this.\n",
      "    * This method has *a lot* of options. You are encouraged to experiment\n",
      "      and play with this method to gain intuition about how it works.\n",
      "    * When dict is used as the `to_replace` value, it is like\n",
      "      key(s) in the dict are the to_replace part and\n",
      "      value(s) in the dict are the value parameter.\n",
      "\n",
      "    Examples\n",
      "    --------\n",
      "\n",
      "    **Scalar `to_replace` and `value`**\n",
      "\n",
      "    >>> s = pd.Series([1, 2, 3, 4, 5])\n",
      "    >>> s.replace(1, 5)\n",
      "    0    5\n",
      "    1    2\n",
      "    2    3\n",
      "    3    4\n",
      "    4    5\n",
      "    dtype: int64\n",
      "\n",
      "    >>> df = pd.DataFrame({'A': [0, 1, 2, 3, 4],\n",
      "    ...                    'B': [5, 6, 7, 8, 9],\n",
      "    ...                    'C': ['a', 'b', 'c', 'd', 'e']})\n",
      "    >>> df.replace(0, 5)\n",
      "        A  B  C\n",
      "    0  5  5  a\n",
      "    1  1  6  b\n",
      "    2  2  7  c\n",
      "    3  3  8  d\n",
      "    4  4  9  e\n",
      "\n",
      "    **List-like `to_replace`**\n",
      "\n",
      "    >>> df.replace([0, 1, 2, 3], 4)\n",
      "        A  B  C\n",
      "    0  4  5  a\n",
      "    1  4  6  b\n",
      "    2  4  7  c\n",
      "    3  4  8  d\n",
      "    4  4  9  e\n",
      "\n",
      "    >>> df.replace([0, 1, 2, 3], [4, 3, 2, 1])\n",
      "        A  B  C\n",
      "    0  4  5  a\n",
      "    1  3  6  b\n",
      "    2  2  7  c\n",
      "    3  1  8  d\n",
      "    4  4  9  e\n",
      "\n",
      "    >>> s.replace([1, 2], method='bfill')\n",
      "    0    3\n",
      "    1    3\n",
      "    2    3\n",
      "    3    4\n",
      "    4    5\n",
      "    dtype: int64\n",
      "\n",
      "    **dict-like `to_replace`**\n",
      "\n",
      "    >>> df.replace({0: 10, 1: 100})\n",
      "            A  B  C\n",
      "    0   10  5  a\n",
      "    1  100  6  b\n",
      "    2    2  7  c\n",
      "    3    3  8  d\n",
      "    4    4  9  e\n",
      "\n",
      "    >>> df.replace({'A': 0, 'B': 5}, 100)\n",
      "            A    B  C\n",
      "    0  100  100  a\n",
      "    1    1    6  b\n",
      "    2    2    7  c\n",
      "    3    3    8  d\n",
      "    4    4    9  e\n",
      "\n",
      "    >>> df.replace({'A': {0: 100, 4: 400}})\n",
      "            A  B  C\n",
      "    0  100  5  a\n",
      "    1    1  6  b\n",
      "    2    2  7  c\n",
      "    3    3  8  d\n",
      "    4  400  9  e\n",
      "\n",
      "    **Regular expression `to_replace`**\n",
      "\n",
      "    >>> df = pd.DataFrame({'A': ['bat', 'foo', 'bait'],\n",
      "    ...                    'B': ['abc', 'bar', 'xyz']})\n",
      "    >>> df.replace(to_replace=r'^ba.$', value='new', regex=True)\n",
      "            A    B\n",
      "    0   new  abc\n",
      "    1   foo  new\n",
      "    2  bait  xyz\n",
      "\n",
      "    >>> df.replace({'A': r'^ba.$'}, {'A': 'new'}, regex=True)\n",
      "            A    B\n",
      "    0   new  abc\n",
      "    1   foo  bar\n",
      "    2  bait  xyz\n",
      "\n",
      "    >>> df.replace(regex=r'^ba.$', value='new')\n",
      "            A    B\n",
      "    0   new  abc\n",
      "    1   foo  new\n",
      "    2  bait  xyz\n",
      "\n",
      "    >>> df.replace(regex={r'^ba.$': 'new', 'foo': 'xyz'})\n",
      "            A    B\n",
      "    0   new  abc\n",
      "    1   xyz  new\n",
      "    2  bait  xyz\n",
      "\n",
      "    >>> df.replace(regex=[r'^ba.$', 'foo'], value='new')\n",
      "            A    B\n",
      "    0   new  abc\n",
      "    1   new  new\n",
      "    2  bait  xyz\n",
      "\n",
      "    Compare the behavior of ``s.replace({'a': None})`` and\n",
      "    ``s.replace('a', None)`` to understand the peculiarities\n",
      "    of the `to_replace` parameter:\n",
      "\n",
      "    >>> s = pd.Series([10, 'a', 'a', 'b', 'a'])\n",
      "\n",
      "    When one uses a dict as the `to_replace` value, it is like the\n",
      "    value(s) in the dict are equal to the `value` parameter.\n",
      "    ``s.replace({'a': None})`` is equivalent to\n",
      "    ``s.replace(to_replace={'a': None}, value=None, method=None)``:\n",
      "\n",
      "    >>> s.replace({'a': None})\n",
      "    0      10\n",
      "    1    None\n",
      "    2    None\n",
      "    3       b\n",
      "    4    None\n",
      "    dtype: object\n",
      "\n",
      "    When ``value`` is not explicitly passed and `to_replace` is a scalar, list\n",
      "    or tuple, `replace` uses the method parameter (default 'pad') to do the\n",
      "    replacement. So this is why the 'a' values are being replaced by 10\n",
      "    in rows 1 and 2 and 'b' in row 4 in this case.\n",
      "\n",
      "    >>> s.replace('a')\n",
      "    0    10\n",
      "    1    10\n",
      "    2    10\n",
      "    3     b\n",
      "    4     b\n",
      "    dtype: object\n",
      "\n",
      "        .. deprecated:: 2.1.0\n",
      "            The 'method' parameter and padding behavior are deprecated.\n",
      "\n",
      "    On the other hand, if ``None`` is explicitly passed for ``value``, it will\n",
      "    be respected:\n",
      "\n",
      "    >>> s.replace('a', None)\n",
      "    0      10\n",
      "    1    None\n",
      "    2    None\n",
      "    3       b\n",
      "    4    None\n",
      "    dtype: object\n",
      "\n",
      "        .. versionchanged:: 1.4.0\n",
      "            Previously the explicit ``None`` was silently ignored.\n",
      "\n",
      "    When ``regex=True``, ``value`` is not ``None`` and `to_replace` is a string,\n",
      "    the replacement will be applied in all columns of the DataFrame.\n",
      "\n",
      "    >>> df = pd.DataFrame({'A': [0, 1, 2, 3, 4],\n",
      "    ...                    'B': ['a', 'b', 'c', 'd', 'e'],\n",
      "    ...                    'C': ['f', 'g', 'h', 'i', 'j']})\n",
      "\n",
      "    >>> df.replace(to_replace='^[a-g]', value='e', regex=True)\n",
      "        A  B  C\n",
      "    0  0  e  e\n",
      "    1  1  e  e\n",
      "    2  2  e  h\n",
      "    3  3  e  i\n",
      "    4  4  e  j\n",
      "\n",
      "    If ``value`` is not ``None`` and `to_replace` is a dictionary, the dictionary\n",
      "    keys will be the DataFrame columns that the replacement will be applied.\n",
      "\n",
      "    >>> df.replace(to_replace={'B': '^[a-c]', 'C': '^[h-j]'}, value='e', regex=True)\n",
      "        A  B  C\n",
      "    0  0  e  f\n",
      "    1  1  e  g\n",
      "    2  2  e  e\n",
      "    3  3  d  e\n",
      "    4  4  e  e\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(df.replace)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "id": "c40cd3c5-85fe-4b6d-9f59-b7f73ede9248",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "id": "cf370b58-4928-416a-9dba-e9c8c7f3286a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame({\"A\": [1.1, np.nan, 3.5, np.nan, np.nan, np.nan, 6.2, 7.9],\n",
    "                   \"B\": [0.25, np.nan, np.nan, .75, 0, np.nan, 6.2, 7.9]})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "id": "7daedf78-3042-4043-8ce1-913cee7b677f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.1</td>\n",
       "      <td>0.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.5</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>0.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NaN</td>\n",
       "      <td>0.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>6.2</td>\n",
       "      <td>6.20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>7.9</td>\n",
       "      <td>7.90</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     A     B\n",
       "0  1.1  0.25\n",
       "1  NaN   NaN\n",
       "2  3.5   NaN\n",
       "3  NaN  0.75\n",
       "4  NaN  0.00\n",
       "5  NaN   NaN\n",
       "6  6.2  6.20\n",
       "7  7.9  7.90"
      ]
     },
     "execution_count": 192,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "id": "dbe4c2be-e3aa-4935-9960-62f09d1d1d12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.100</td>\n",
       "      <td>0.250000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.300</td>\n",
       "      <td>0.416667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.500</td>\n",
       "      <td>0.583333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.175</td>\n",
       "      <td>0.750000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4.850</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>5.525</td>\n",
       "      <td>3.100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>6.200</td>\n",
       "      <td>6.200000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>7.900</td>\n",
       "      <td>7.900000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       A         B\n",
       "0  1.100  0.250000\n",
       "1  2.300  0.416667\n",
       "2  3.500  0.583333\n",
       "3  4.175  0.750000\n",
       "4  4.850  0.000000\n",
       "5  5.525  3.100000\n",
       "6  6.200  6.200000\n",
       "7  7.900  7.900000"
      ]
     },
     "execution_count": 194,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.interpolate()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "id": "bf36f6bb-59e1-4962-9f7b-2b3e0482b262",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>k1</th>\n",
       "      <th>k2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>one</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>two</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>one</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>two</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>one</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>two</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>two</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>one</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    k1  k2\n",
       "0  one   1\n",
       "1  two   1\n",
       "2  one   2\n",
       "3  two   3\n",
       "4  one   3\n",
       "5  two   4\n",
       "6  two   4\n",
       "7  one   2"
      ]
     },
     "execution_count": 200,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame({\"k1\": ['one', 'two'] * 3 + ['two']+['one'],\n",
    "                  \"k2\": [1, 1, 2, 3, 3, 4, 4, 2]})\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "id": "30822e63-aa34-4c89-b652-942ddca5b526",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    False\n",
       "1    False\n",
       "2    False\n",
       "3    False\n",
       "4    False\n",
       "5    False\n",
       "6     True\n",
       "7     True\n",
       "dtype: bool"
      ]
     },
     "execution_count": 202,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "id": "8e8b849c-2f55-47d0-a8da-73f3f444d309",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "pandas.core.series.Series"
      ]
     },
     "execution_count": 204,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(df.duplicated())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "id": "a82e3103-1fa2-42d0-98d3-4b3d59fa12df",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([False,  True])"
      ]
     },
     "execution_count": 208,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "id": "93b95065-dc42-43bc-a3aa-21c3c722b0f9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>k1</th>\n",
       "      <th>k2</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>one</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>two</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>one</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>two</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>one</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>two</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    k1  k2\n",
       "0  one   1\n",
       "1  two   1\n",
       "2  one   2\n",
       "3  two   3\n",
       "4  one   3\n",
       "5  two   4"
      ]
     },
     "execution_count": 210,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop_duplicates()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "id": "a7927cfb-6ba9-488b-b2d3-40d3cf7e2a1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on method drop_duplicates in module pandas.core.frame:\n",
      "\n",
      "drop_duplicates(subset: 'Hashable | Sequence[Hashable] | None' = None, *, keep: 'DropKeep' = 'first', inplace: 'bool' = False, ignore_index: 'bool' = False) -> 'DataFrame | None' method of pandas.core.frame.DataFrame instance\n",
      "    Return DataFrame with duplicate rows removed.\n",
      "\n",
      "    Considering certain columns is optional. Indexes, including time indexes\n",
      "    are ignored.\n",
      "\n",
      "    Parameters\n",
      "    ----------\n",
      "    subset : column label or sequence of labels, optional\n",
      "        Only consider certain columns for identifying duplicates, by\n",
      "        default use all of the columns.\n",
      "    keep : {'first', 'last', ``False``}, default 'first'\n",
      "        Determines which duplicates (if any) to keep.\n",
      "\n",
      "        - 'first' : Drop duplicates except for the first occurrence.\n",
      "        - 'last' : Drop duplicates except for the last occurrence.\n",
      "        - ``False`` : Drop all duplicates.\n",
      "\n",
      "    inplace : bool, default ``False``\n",
      "        Whether to modify the DataFrame rather than creating a new one.\n",
      "    ignore_index : bool, default ``False``\n",
      "        If ``True``, the resulting axis will be labeled 0, 1, …, n - 1.\n",
      "\n",
      "    Returns\n",
      "    -------\n",
      "    DataFrame or None\n",
      "        DataFrame with duplicates removed or None if ``inplace=True``.\n",
      "\n",
      "    See Also\n",
      "    --------\n",
      "    DataFrame.value_counts: Count unique combinations of columns.\n",
      "\n",
      "    Examples\n",
      "    --------\n",
      "    Consider dataset containing ramen rating.\n",
      "\n",
      "    >>> df = pd.DataFrame({\n",
      "    ...     'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],\n",
      "    ...     'style': ['cup', 'cup', 'cup', 'pack', 'pack'],\n",
      "    ...     'rating': [4, 4, 3.5, 15, 5]\n",
      "    ... })\n",
      "    >>> df\n",
      "        brand style  rating\n",
      "    0  Yum Yum   cup     4.0\n",
      "    1  Yum Yum   cup     4.0\n",
      "    2  Indomie   cup     3.5\n",
      "    3  Indomie  pack    15.0\n",
      "    4  Indomie  pack     5.0\n",
      "\n",
      "    By default, it removes duplicate rows based on all columns.\n",
      "\n",
      "    >>> df.drop_duplicates()\n",
      "        brand style  rating\n",
      "    0  Yum Yum   cup     4.0\n",
      "    2  Indomie   cup     3.5\n",
      "    3  Indomie  pack    15.0\n",
      "    4  Indomie  pack     5.0\n",
      "\n",
      "    To remove duplicates on specific column(s), use ``subset``.\n",
      "\n",
      "    >>> df.drop_duplicates(subset=['brand'])\n",
      "        brand style  rating\n",
      "    0  Yum Yum   cup     4.0\n",
      "    2  Indomie   cup     3.5\n",
      "\n",
      "    To remove duplicates and keep last occurrences, use ``keep``.\n",
      "\n",
      "    >>> df.drop_duplicates(subset=['brand', 'style'], keep='last')\n",
      "        brand style  rating\n",
      "    1  Yum Yum   cup     4.0\n",
      "    2  Indomie   cup     3.5\n",
      "    4  Indomie  pack     5.0\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(df.drop_duplicates)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e76c137-19bb-437d-9c47-3d1c0792c793",
   "metadata": {},
   "source": [
    "## Visualization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "id": "589b3112-970e-49c2-ba2b-4f485e052361",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='LoanID'>"
      ]
     },
     "execution_count": 217,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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ww8/jCzLfPbZZwBYrVZatGjBJ598wp49e3j22Wf5xz/+wSeffAJAnz59aN26tUogM5vNLFq0iHvuuQeABx98EKPRyP/+9z927drFK6+8QmxsLACRkZG8//77vPPOOyxfvpy///3v/OMf/+Cyyy5T5Wv69Ol06tSJHTt2OO2QLhAIqvFpryuBQFC3kMvK2Netu8/xIir/P1v584esH3cgRUf7GdvGjBkzyMnJYezYsQA8+uijbNmyhRkzZnDNNdfQtGlTABo1akRqaqoSr0uXLnTp0kU5njJlCsuWLePzzz/noYce8ikPSUlJJCcnc+jQIQAiIiJ4/vnnleuZmZls2rSJTz75hOHDhwMwatQoFixYwGOPPQbAypUrKS0tVa4fOXKEW2+9lc6dOwPQunVr1T0vu+wynnrqKW699Va6du3KP//5T6d8XXvttUyaNMmnZxEIGiJCoxMizBZrUEa84U6J0Rzwc8qyjNliVR1brL6nGcwyt8+Pp3OBptnQ2bt3L71791ad6927N3v37vUYr6SkhMcff5yOHTvSqFEjYmNj+e233/zS6ICtzkmSpBz/61//4rLLLqNp06bExsYyb948Vdo5OTn88ccfbNmyBYB3332X4cOHExMTA8D48eOZMmUKvXv35rnnnuOXX35xuuc///lPrFYrTz75JDqd85jUUcMjEAhcIzQ6IaDYaKbPq9/SrWUi/767/jZWH207wj+W7WLYJWm8MaKr3+k89OFPbPzjNP977BoSoiO49a1NnCo28s3EfkRovZPVy00W+rz6Le1T4lh0bw+/8wLw5a5cHvzwR16/oys3dkkD4MUVe/hgy2HWTOhDRpMYn9P881Qx18/+jnuuyuCp6zsElD97pKgosn7c4XO83ccLAUhJiKRprMHvewcDewEDnIUOVzz22GN89dVXzJgxg7Zt2xIVFcVtt93ml9HumTNnOHXqFJmZmQB88sknPPLII8ycOZOePXsSFxfH9OnT2bp1qxInOTmZYcOGsWDBAlq3bs2XX36p2jX93nvvZdCgQaxcuZI1a9Ywbdo0Zs6cybhx45QwERE2vZorIQdQhCaBQOAZodEJAev2nORsSQXr9p4MdVZqlQ82H0aW4fOfTwSUzspduRSWmVixy5bOj0fOcfRsGfvyznudxuYDZ8g/b2TjH6cDygvA2MU/Issw/qOflHPzNx6k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XHnllSQmJrJs2TJGjBhBs2bNAOjYsaMS3mAw0Lp161o3zBaElkBaNTkUy67qGELQCQHh3lkL/CfcNE6SJPk0fQS2hlOrt8XR6bVK/KpzWp3GbZoRRi0RleG86fjBZoT7/vvvM3PmTAYOHKi6duutt7J48WI6derk0zNUodfrVaua7ElPT6dNmzZO57/77jtuuukmZRrNarXy+++/k5XRzmU6HTp0wGw288MPP3DFFVcANg3VuXPnasyfLMsYjbbNart3747BYGDfvn1cddVVgM1m6NChQ7Rq1arGtAR1l4DkkzByoxOucpZPU1eTJ09WVi9U/armvsH20U6ePJm0tDSioqLo16+fkyGd0Whk3LhxNGnShJiYGG688UaOHVOrhAsKCsjOzlZGP9nZ2U6NxpEjRxg2bBgxMTE0adKE8ePHux1xCUJDbXT6wUgz3DcGbWisWLGCgoICRo0aRadOnVS/2267jfnz5/uddkZGBlu3buXQoUOcPn3aK21P27ZtWbt2LZs2bWLv3r3cd9995OXluQ2flZXF4MGDGT16NFu3bmXHjh3ce++9REVFKWEOHDjAtGnT2LFjB0eOHGHz5s0MHz6cqKgohgwZAkB8fDz3338/zz33HGvWrGHfvn088MADANx+++1+l4GgfuPTwDlcJZFaxmcbnYsvvlhZwZCbm8uuXbuUa6+++iqvvfYac+fOZfv27aSmpjJgwADOnz+vhJkwYQLLli1jyZIlbNy4keLiYoYOHaoadY0cOZKdO3eyevVqVq9ezc6dO8nOzlauWywWbrjhBkpKSti4cSNLlizh008/ZeLEif6WwwVFTF35TzBEFCHnhBfz58+nf//+JCQkOF279dZb2blzJz/++KNfaU+aNAmtVkvHjh1p2rQpR48frTHOM888Q7du3Rg0aBD9+vUjNTWVm2++2WOcBQsWkJ6eTt++fbnlllsYM2YMycnJyvXIyEi+++47hgwZQtu2bRk+fDgxMTFs2rRJFW769OnccccdZGdnc/nll3P48GG++eYbEhMT/Xp+Qd3ggjVJDbTt83nqSqfTqbQ4VciyzOzZs3n66acVT57vvfceKSkpfPjhh9x3330UFhYyf/58PvjgA2UlxaJFi0hPT2fdunUMGjSIvXv3snr1atUKhnnz5tGzZ0/27dtHVlYWa9asYc+ePRw9epS0tDTANq+e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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "lending_co_data.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 221,
   "id": "af8f6e5a-ecc7-46e4-8fb8-90558a1d3b16",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 221,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df = pd.DataFrame(np.random.randn(10,4), index=pd.date_range('1/1/2000', periods=10), columns=list('ABCD'))\n",
    "df.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 233,
   "id": "27157254-e298-4555-93eb-9936c7ff5e61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          A         B         C         D\n",
      "0  0.315860  0.365860  0.123737  0.728112\n",
      "1  0.540781  0.907826  0.393730  0.541811\n",
      "2  0.667057  0.501804  0.607029  0.176743\n",
      "3  0.406675  0.078876  0.515071  0.581525\n",
      "4  0.976613  0.824281  0.359719  0.140124\n",
      "5  0.322037  0.119099  0.197622  0.047323\n",
      "6  0.194408  0.929946  0.600698  0.151895\n",
      "7  0.881801  0.355747  0.739005  0.463553\n",
      "8  0.378425  0.552933  0.363959  0.947995\n",
      "9  0.261592  0.589454  0.080650  0.271708\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 233,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df = pd.DataFrame(np.random.rand(10,4), columns=list('ABCD'))\n",
    "print(df)\n",
    "df.plot.bar()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 227,
   "id": "1dc816ba-ef5e-415b-aed1-ba5f8c78c620",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 227,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiMAAAGYCAYAAACQz+KaAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAkPUlEQVR4nO3dfVDVZf7/8dcRCLC4SRI4JOpxMiS1MnSTLG+iUEwbZ22qndq00hnTLCW3sna3tqnF2XFbc1XoRiXTTHexzFDTLW8ra0Att9C10iCCyG4gsUDh+v3ReH7xlbtz5JwLDs/HzOePz/X5XFzvaxB5cX1ujsMYYwQAAGBJF9sFAACAzo0wAgAArCKMAAAAqwgjAADAKsIIAACwijACAACsIowAAACrCCMAAMCqYNsFtEZ9fb2++uorRUREyOFw2C4HAAC0gjFGP/74oxISEtSlS9PrHx0ijHz11VdKTEy0XQYAAPBCSUmJevTo0eTxDhFGIiIiJP0ymcjISMvVAACA1qiqqlJiYqL793hTOkQYOX1pJjIykjACAEAH09ItFtzACgAArCKMAAAAqwgjAADAqg5xzwgAAB1NXV2dTp48absMnwoJCVFQUNBZfx3CCAAAbcgYo/Lycv3www+2S/GL6OhoxcfHn9V7wAgjAAC0odNBJDY2Vl27dg3Yl3UaY3TixAlVVFRIkpxOp9dfizACAEAbqaurcweRmJgY2+X4XHh4uCSpoqJCsbGxXl+y4QZWAADayOl7RLp27Wq5Ev85PdezuT+GMAIAQBsL1EszjWmLuRJGAACAVYQRAABgFTewAgDgB70fzvfbWEfn3eB133fffVfXXHONrr/+em3evLkNq2oaKyMAAMBt2bJlmjlzpnbv3q3i4mK/jEkYAQAAkqTq6mqtXbtW99xzj8aNG6fc3Fy/jEsYAQAAkqQ1a9YoKSlJSUlJuv3227V8+XIZY3w+rkdhJCsrS0OGDFFERIRiY2M1YcIEHTp0qNk+27dvl8PhOGM7ePDgWRUOAADa1tKlS3X77bdLksaMGaPjx4/rrbfe8vm4HoWRHTt2aMaMGdqzZ4+2bt2qU6dOKT09XdXV1S32PXTokMrKytxb3759vS4aAAC0rUOHDumDDz7QrbfeKkkKDg7WLbfcomXLlvl8bI+epvm/d9UuX75csbGxKiws1PDhw5vtGxsbq+joaI8LBAAAvrd06VKdOnVKF154obvNGKOQkBB9//33Ov/883029lndM1JZWSlJ6tatW4vnDho0SE6nU2lpadq2bVuz59bU1KiqqqrBBgAAfOPUqVNasWKF/v73v2v//v3u7cMPP1SvXr20atUqn47vdRgxxigzM1NXX321BgwY0OR5TqdTzz33nPLy8rRu3TolJSUpLS1NO3fubLJPVlaWoqKi3FtiYqK3ZQIAgBa88cYb+v7773X33XdrwIABDbabbrpJS5cu9en4DuPlbbIzZsxQfn6+du/erR49enjUd/z48XI4HHr99dcbPV5TU6Oamhr3flVVlRITE1VZWanIyEhvygUAwOd+/vlnHTlyRC6XS2FhYbbLabXx48ervr5e+flnvpht7969SklJUWFhoa644oozjjc356qqKkVFRbX4+9urN7DOnDlTr7/+unbu3OlxEJGkoUOHauXKlU0eDw0NVWhoqDelAQAAD23YsKHJY1dccYXPH+/1KIwYYzRz5ky9+uqr2r59u1wul1eD7tu3T06n06u+AAAgsHgURmbMmKGXX35Z69evV0REhMrLyyVJUVFRCg8PlyTNnTtXpaWlWrFihSRpwYIF6t27t/r376/a2lqtXLlSeXl5ysvLa+OpAACAjsijMJKdnS1JGjlyZIP25cuXa/LkyZKksrKyBu+yr62t1Zw5c1RaWqrw8HD1799f+fn5Gjt27NlVDgAAAoLXN7D6U2tvgAEAwKaOegPr2WiLG1j5bBoAAGAVYQQAAFhFGAEAAFYRRgAAgFWEEQAAYBVhBAAAaPLkyXI4HO4tJiZGY8aM0UcffeTzsb16HTwAAPDQ41F+HKvSq25jxozR8uXLJUnl5eX64x//qHHjxjV4f5gvsDICAAAk/fLZcPHx8YqPj9fll1+uhx56SCUlJfrmm298Oi5hBAAAnOH48eNatWqVLrroIsXExPh0LC7TAAAASdIbb7yh8847T5JUXV0tp9OpN954Q126+HbtgjDSzvV+OL/R9qPzbvBzJQCAQDdq1Cj359B99913WrJkiTIyMvTBBx+oV69ePhuXMAIAACRJ5557ri666CL3fkpKiqKiovT888/rySef9Nm43DMCAAAa5XA41KVLF/30008+HYeVEQAAIEmqqalReXm5JOn777/XokWLdPz4cY0fP96n4xJGAACAJGnz5s1y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IxDmILWveTiMael5GwAAAN/hs2kAAIBVhBEAAGAVYQQAAFhFGAEAAFYRRgA0i3vcAfiaV6+DDwRffvmlsrOz9e6776q8vFwOh0NxcXG66qqrNG3aNCUmJtouEWgXQkND9eGHHyo5Odl2KQDOQllZmbKzs7V7926VlZUpKChILpdLEyZM0OTJkxUUFGSttk75aO/u3buVkZGhxMREpaenKy4uTsYYVVRUaOvWrSopKdGmTZs0bNgw26WelZKSEj322GNatmyZ7VKa9dNPP6mwsFDdunXTJZdc0uDYzz//rLVr1zZ4kV57VVRUpD179ig1NVX9+vXTwYMH9cwzz6impka33367rr32WtslNuvXnwf1a88884xuv/1298c3PP300/4s66x9//33evHFF3X48GE5nU5NmjSp3f+xsW/fPkVHR8vlckmSVq5cqezsbBUXF6tXr1669957deutt1qusmUzZ87UzTffrGuuucZ2KWfln//8pwoKCnTDDTfo5ptv1ksvvaSsrCzV19frt7/9rZ544gkFB7fvv+0LCgp03XXXyeVyKTw8XO+//75uu+021dbW6s0331RycrLefPNNRURE2Cmw5c/qDTyDBw82s2bNavL4rFmzzODBg/1YkW/s37/fdOnSxXYZzTp06JDp1auXcTgcpkuXLmbEiBENPs25vLy83c/BGGM2bdpkzjnnHNOtWzcTFhZmNm3aZLp3726uu+46k5aWZoKDg81bb71lu8xmORwOc/nll5uRI0c22BwOhxkyZIgZOXKkGTVqlO0yW+R0Os2xY8eMMcZ8/vnnJj4+3sTHx5vrr7/e9OjRw0RFRZmioiLLVTZv0KBB5u233zbGGPP888+b8PBwc99995ns7Gwza9Ysc95555mlS5darrJlp3+u+/bta+bNm2fKyspsl+SxJ554wkRERJiJEyea+Ph4M2/ePBMTE2OefPJJ89e//tV0797d/PnPf7ZdZouGDRtmHn/8cff+Sy+9ZK688kpjjDHfffedufzyy819991nqzzTKcNIWFiYOXjwYJPHi4qKTFhYmB8r8s769eub3f7xj3+0+1/kEyZMMOPGjTPffPONOXz4sBk/frxxuVzmiy++MMZ0nDCSmppqHn30UWOMMatXrzbnn3++eeSRR9zHH3nkEXP99dfbKq9V/vrXvxqXy3VGaAoODjYff/yxpao853A4zNdff22MMebWW281I0eONNXV1cYYY37++Wczbtw4c9NNN9kssUVdu3Z1/wwMGjTIPPvssw2Or1q1ylxyySU2SvOIw+Ew//nPf8z9999vLrjgAhMSEmJuvPFGs2HDBlNXV2e7vFbp06ePycvLM8b88gdeUFCQWblypfv4unXrzEUXXWSrvFYLDw83n332mXu/rq7OhISEmPLycmOMMVu2bDEJCQm2yuucYcTlcplly5Y1eXzZsmXG5XL5sSLvnP6rw+FwNLm191/ksbGx5qOPPmrQNn36dNOzZ0/z2WefdZgwEhkZaQ4fPmyM+eWHPDg42BQWFrqPHzhwwMTFxdkqr9U++OADc/HFF5sHHnjA1NbWGmM6dhhpLFzt2bPH9OjRw0ZprRYTE2MKCgqMMb/8jOzfv7/B8U8//dSEh4fbKM0jv/5e1NbWmjVr1pjRo0eboKAgk5CQYB555BH3z017FR4e7g6GxhgTEhJi/vvf/7r3jx49arp27WqjNI/06tXL7N69273/1VdfGYfDYU6cOGGMMebIkSNW/wjvlE/TzJkzR9OmTdO9996r9evXa8+ePXr//fe1fv163Xvvvbrnnnv04IMP2i6zRU6nU3l5eaqvr29027t3r+0SW/TTTz+dca118eLFuvHGGzVixAj973//s1SZ97p06aKwsDBFR0e72yIiIlRZWWmvqFYaMmSICgsL9c0332jw4ME6cOCAHA6H7bI8drrmmpoaxcXFNTgWFxenb775xkZZrZaRkaHs7GxJ0ogRI/Tvf/+7wfG1a9fqoosuslGa10JCQnTzzTdr8+bN+vzzzzV16lStWrVKSUlJtktrVnx8vD755BNJ0uHDh1VXV+fel6SPP/5YsbGxtsprtQkTJmjatGnavHmztm3bpttuu00jRoxQeHi4JOnQoUO68MIL7RVoLQZZ9sorr5grr7zSBAcHu1cRgoODzZVXXmnWrFlju7xWGT9+vPnTn/7U5PH9+/cbh8Phx4o8N2TIELNixYpGj82YMcNER0d3iJWRSy+91GzatMm9f+DAAXPy5En3/q5duzrEatuvrV692sTFxZkuXbp0uJWRgQMHmkGDBpnzzjvPrFu3rsHxHTt2mAsvvNBSda1TWlpqevfubYYPH24yMzNNeHi4ufrqq83UqVPN8OHDzTnnnGPy8/Ntl9miX6+MNKa+vt5s2bLFjxV57tFHHzXdu3c3U6ZMMS6Xy8ydO9f07NnTZGdnm5ycHJOYmGhmz55tu8wW/fjjj+bmm292/8676qqrzOeff+4+/uabb5q1a9daq69TPk3zaydPntSxY8ckSRdccIFCQkIsV9R6u3btUnV1tcaMGdPo8erqahUUFGjEiBF+rqz1srKytGvXLm3cuLHR49OnT1dOTo7q6+v9XJlncnJylJiYqBtuuKHR448++qi+/vprvfDCC36u7Ox8+eWXKiws1HXXXadzzz3Xdjmt8pe//KXB/tChQzV69Gj3/h/+8Ad9+eWXWr16tb9L88gPP/ygefPmacOGDfr8889VX18vp9OpYcOGafbs2Ro8eLDtElvkcrlUUFDgfhKrI6qrq9O8efO0Z88eXX311XrooYf0yiuv6MEHH9SJEyc0fvx4LVq0qMP8fPz88886deqUzjvvPNulNNDpwwgAALCrU94zAgAA2g/CCAAAsIowAgAArCKMAAAAqwgjAADAKsIIAACwijACAACsIowAAACr/h9c4hJ5KfM2zAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.plot.bar(ylim=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
   "id": "f3d01e2e-4e31-424b-bc15-8a3dea044b7e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 235,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiMAAAGYCAYAAACQz+KaAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAkk0lEQVR4nO3dfXBV1b3/8c8hiUnUkEgkyYkGOI40RKiKgatRgVA0EIQOUzpop97CrThDeSqkXNqAvVanGKZDLaVgUttARJRiG1pUnm8rTxV0AqHm9gYu1mBiTIxUTSSYR9b9gx/n57nk6Zyws5KT92tm/7GfzvquweP5ZO2913YZY4wAAAAsGWC7AAAA0L8RRgAAgFWEEQAAYBVhBAAAWEUYAQAAVhFGAACAVYQRAABgFWEEAABYFWq7gK64ePGiPvzwQ0VFRcnlctkuBwAAdIExRp9//rkSExM1YED74x99Iox8+OGHSkpKsl0GAAAIQEVFhW6++eZ29/eJMBIVFSXpUmcGDhxouRoAANAVdXV1SkpK8v6Ot6dPhJHLl2YGDhxIGAEAoI/p7BYLbmAFAABW+RVGcnJyNHbsWEVFRSkuLk4zZszQ6dOnOzznwIEDcrlcVyynTp3qVuEAACA4+BVGDh48qAULFujYsWPav3+/WlpalJGRofr6+k7PPX36tKqqqrzL8OHDAy4aAAAED7/uGdmzZ4/P+qZNmxQXF6fjx49r/PjxHZ4bFxenmJgYvwsEAKAvam1tVXNzs+0yHBUWFqaQkJBuf063bmCtra2VJA0aNKjTY0ePHq2GhgbddttteuKJJzRx4sTuNA0AQK9kjFF1dbU+++wz26X0iJiYGCUkJHRrHrCAw4gxRllZWbr//vs1atSodo9zu916/vnnlZqaqsbGRr344ouaNGmSDhw40O5oSmNjoxobG73rdXV1gZYJAECPuhxE4uLidO211wbtZJ3GGF24cEE1NTWSLv3eByrgMLJw4UK98847OnLkSIfHJScnKzk52buelpamiooKrVmzpt0wkpOTo6eeeirQ0gAAsKK1tdUbRGJjY22X47jIyEhJUk1NjeLi4gK+ZBPQo72LFi3Sq6++qjfeeKPDGdXac8899+jMmTPt7s/OzlZtba13qaioCKRMAAB61OV7RK699lrLlfScy33tzv0xfo2MGGO0aNEi/fGPf9SBAwfk8XgCarS4uLjD4Zzw8HCFh4cH9NkAANgWrJdm2nI1+upXGFmwYIFefvll7dixQ1FRUaqurpYkRUdHe4dqsrOzVVlZqc2bN0uS1q5dq2HDhmnkyJFqamrSli1bVFhYqMLCwm4XDwAA+j6/wkhubq4kKT093Wf7pk2bNGfOHElSVVWVysvLvfuampq0bNkyVVZWKjIyUiNHjtTOnTs1derU7lUOAACCgssYY2wX0Zm6ujpFR0ertraWd9MAAHqthoYGlZWVyePxKCIiwmffsB/t7LE6zq5+KOBz33zzTY0bN04PPvjgFfOLtaWjPnf195t30wAAAK+NGzdq0aJFOnLkiM+VDicRRgAAgCSpvr5er7zyir73ve9p2rRpKigo6JF2uzUDKwCgfysdkeJ4GymnSh1vA5ds27bNOz/Yo48+qkWLFunHP/6x408HMTICAAAkSfn5+Xr00UclSVOmTNH58+f15z//2fF2CSMAAECnT5/W22+/rUceeUSSFBoaqocfflgbN250vG0u0wAAAOXn56ulpUU33XSTd5sxRmFhYfr00091ww03ONY2IyMAAPRzLS0t2rx5s37+85/r5MmT3uVvf/ubhg4dqpdeesnR9hkZAQCgn3v99df16aef6rHHHlN0dLTPvm9+85vKz8/XwoULHWufMAIAQA/ozkRkTsvPz9cDDzxwRRCRpJkzZ+qZZ57RiRMndNdddznSPmEEAIB+7rXXXmt331133SWnJ2snjPRyPMMPAAh23MAKAACsIowAAACrCCMAAMAqwggAALCKMAIAAKwijAAAAKsIIwAAwCrCCAAAsIowAgAANGfOHLlcLu8SGxurKVOm6J133nG8bWZgBQCgJ/zkyve+ONdWbUCnTZkyRZs2bZIkVVdX64knntC0adNUXl5+Nau7AiMjAABAkhQeHq6EhAQlJCTozjvv1A9/+ENVVFTo448/drRdwggAALjC+fPn9dJLL+nWW29VbGyso21xmQboZ5x++SIvXgT6rtdff13XX3+9JKm+vl5ut1uvv/66BgxwduyCkREAACBJmjhxok6ePKmTJ0/qrbfeUkZGhjIzM/X+++872i4jIwAAQJJ03XXX6dZbb/Wup6amKjo6Wr/5zW/005/+1LF2GRkBAABtcrlcGjBggL744gtH22FkBAAASJIaGxtVXV0tSfr000+1fv16nT9/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DBjQ50ZGvvrVr5rRo0eb66+/3mzfvt1n/8GDB81NN91kqbquqaysNMOGDTPjx483WVlZJjIy0tx///3m8ccfN+PHjzfXXHON2blzp+0yO/XlkZG2XLx40ezbt68HK/LfypUrzeDBg83cuXONx+Mx2dnZZsiQISY3N9fk5eWZpKQks3TpUttldurzzz83s2bN8v7m3Xvvvea9997z7t+7d6955ZVXrNXXL5+m+bLm5madO3dOknTjjTcqLCzMckVdd/jwYdXX12vKlClt7q+vr1dRUZEmTJjQw5V1XU5Ojg4fPqxdu3a1uX/+/PnKy8vTxYsXe7gy/+Tl5SkpKUkPPfRQm/tXrlypjz76SL/97W97uLLu+eCDD3T8+HE98MADuu6662yX0yVPPfWUz/o999yjyZMne9f//d//XR988IG2bt3a06X55bPPPtPq1av12muv6b333tPFixfldrt13333aenSpRozZoztEjvl8XhUVFTkfRKrL2ptbdXq1at17Ngx3X///frhD3+o3/3ud1q+fLkuXLig6dOna/369X3m+9HQ0KCWlhZdf/31tkvx0e/DCAAAsKtf3jMCAAB6D8IIAACwijACAACsIowAAACrCCMAAMAqwggAALCKMAIAAKwijAAAAKv+F8zmIqfJb+J0AAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.plot.bar(stacked=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 237,
   "id": "d15c3f62-dfab-4cb0-8b8e-d8a4b2930cae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 237,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAhYAAAGdCAYAAABO2DpVAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAhh0lEQVR4nO3de3QU9f3/8dfmtiGYLBe5BFkgiidBAqgBCwhWBKNROLQHr3gJqOeIBBRprURb8VJc8VhLrRoLJwKKCljAWq1EvADyRZRLUCwBoXJJISlicReiXUyY3x+/w/akJMhsPrOTDc/HOfPHTj6z73cyzNkXn5md8ViWZQkAAMCABLcbAAAALQfBAgAAGEOwAAAAxhAsAACAMQQLAABgDMECAAAYQ7AAAADGECwAAIAxSbEueOzYMe3fv1/p6enyeDyxLg8AAKJgWZYOHz6sLl26KCGh8XmJmAeL/fv3y+/3x7osAAAwoLKyUl27dm305zEPFunp6ZL+f2MZGRmxLg8AAKIQCoXk9/sjn+ONiXmwOH76IyMjg2ABAECc+bHLGLh4EwAAGEOwAAAAxhAsAACAMQQLAABgDMECAAAYQ7AAAADGxPzrpsflTi9TgjfNrfJG7E4d63YLMKBPVrcmbb84UGuok+aj17YKt1sAEKeYsQAAAMYQLAAAgDEECwAAYAzBAgAAGGM7WBw+fFhTpkxR9+7d1apVKw0ePFjr1693ojcAABBnbAeLO+64QytWrNDLL7+sLVu2KD8/XyNGjNC+ffuc6A8AAMQRW8Hi+++/15IlS/Tkk0/qkksuUc+ePfXwww8rKytLJSUlTvUIAADihK37WNTW1qqurk6pqan11rdq1Upr1qxpcJtwOKxwOBx5HQqFomgTAADEA1szFunp6Ro0aJAee+wx7d+/X3V1dVqwYIE++eQTVVVVNbhNIBCQz+eLLH6/30jjAACg+bF9jcXLL78sy7J01llnyev16plnntHYsWOVmJjY4Pji4mIFg8HIUllZ2eSmAQBA82T7lt7nnHOOVq1apZqaGoVCIWVmZur6669XVlZWg+O9Xq+8Xm+TGwUAAM1f1PexaN26tTIzM3Xo0CGVlZVp9OjRJvsCAABxyPaMRVlZmSzLUnZ2tnbu3Kn77rtP2dnZGj9+vBP9AQCAOGJ7xiIYDKqoqEg5OTm69dZbNWTIEL377rtKTk52oj8AABBHbM9YXHfddbruuuuc6AUAAMQ5nhUCAACMIVgAAABjPJZlWbEsGAqF5PP5FAwGlZGREcvSAAAgSqf6+c2MBQAAMIZgAQAAjCFYAAAAYwgWAADAGIIFAAAwhmABAACMIVgAAABjCBYAAMAYggUAADCGYAEAAIwhWAAAAGMIFgAAwBiCBQAAMIZgAQAAjCFYAAAAYwgWAADAGIIFAAAwhmABAACMSXKrcO70MiV409wq3+ztTh3rdgs4RX2yurndQrO0OFDrdguAY3ptq3C7hWaLGQsAAGAMwQIAABhDsAAAAMYQLAAAgDG2gkVtba1+/etfKysrS61atdLZZ5+tRx99VMeOHXOqPwAAEEdsfStk5syZeuGFFzR//nz17t1bGzZs0Pjx4+Xz+XTPPfc41SMAAIgTtoLFxx9/rNGjR+vqq6+WJPXo0UOvvfaaNmzY4EhzAAAgvtg6FTJkyBC9//77+vLLLyVJn332mdasWaOrrrqq0W3C4bBCoVC9BQAAtEy2Zizuv/9+BYNB5eTkKDExUXV1dZoxY4ZuvPHGRrcJBAJ65JFHmtwoAABo/mzNWCxatEgLFizQq6++qk2bNmn+/Pl66qmnNH/+/Ea3KS4uVjAYjCyVlZVNbhoAADRPtmYs7rvvPk2bNk033HCDJKlPnz7as2ePAoGACgsLG9zG6/XK6/U2vVMAANDs2Zqx+O6775SQUH+TxMREvm4KAAAk2ZyxGDVqlGbMmKFu3bqpd+/eKi8v19NPP63bbrvNqf4AAEAcsRUs/vjHP+o3v/mNJk6cqAMHDqhLly6688479dBDDznVHwAAiCO2gkV6erpmzZqlWbNmOdQOAACIZzwrBAAAGEOwAAAAxngsy7JiWTAUCsnn8ykYDCojIyOWpQEAQJRO9fObGQsAAGAMwQIAABhDsAAAAMYQLAAAgDEECwAAYAzBAgAAGEOwAAAAxhAsAACAMQQLAABgDMECAAAYQ7AAAADGECwAAIAxBAsAAGAMwQIAABhDsAAAAMYQLAAAgDEECwAAYAzBAgAAGJPkVuHc6WVK8Ka5VR74UbtTx7rdQrPTJ6ub2y0gTi0O1Lrdwmmh17YKt1tgxgIAAJhDsAAAAMYQLAAAgDEECwAAYIytYNGjRw95PJ4TlqKiIqf6AwAAccTWt0LWr1+vurq6yOsvvvhCl19+ua699lrjjQEAgPhjK1h06NCh3usnnnhC55xzjn76058abQoAAMSnqO9jcfToUS1YsEBTp06Vx+NpdFw4HFY4HI68DoVC0ZYEAADNXNQXb77xxhv69ttvNW7cuJOOCwQC8vl8kcXv90dbEgAANHNRB4vS0lIVFBSoS5cuJx1XXFysYDAYWSorK6MtCQAAmrmoToXs2bNH7733npYuXfqjY71er7xebzRlAABAnIlqxmLu3Lnq2LGjrr76atP9AACAOGY7WBw7dkxz585VYWGhkpJce4YZAABohmwHi/fee0979+7Vbbfd5kQ/AAAgjtmecsjPz5dlWU70AgAA4hzPCgEAAMYQLAAAgDEeK8bnNUKhkHw+n4LBoDIyMmJZGgAAROlUP7+ZsQAAAMYQLAAAgDEECwAAYAzBAgAAGEOwAAAAxhAsAACAMQQLAABgDMECAAAYQ7AAAADGECwAAIAxBAsAAGAMwQIAABhDsAAAAMYQLAAAgDEECwAAYAzBAgAAGEOwAAAAxhAsAACAMUluFc6dXqYEb5pb5U+wO3Ws2y0AxvTJ6uZ2CzBscaA25jV7bauIeU3EP2YsAACAMQQLAABgDMECAAAYQ7AAAADG2A4W+/bt080336z27dsrLS1N559/vjZu3OhEbwAAIM7Y+lbIoUOHdPHFF2vYsGF655131LFjR/3jH/9QmzZtHGoPAADEE1vBYubMmfL7/Zo7d25kXY8ePUz3BAAA4pStUyFvvvmm+vfvr2uvvVYdO3bUBRdcoDlz5px0m3A4rFAoVG8BAAAtk61g8dVXX6mkpETnnnuuysrKNGHCBN1999166aWXGt0mEAjI5/NFFr/f3+SmAQBA8+SxLMs61cEpKSnq37+/1q5dG1l39913a/369fr4448b3CYcDiscDkdeh0Ih+f1++acs5s6bgEO482bLw5034bZQKCSfz6dgMKiMjIxGx9mascjMzNR5551Xb12vXr20d+/eRrfxer3KyMiotwAAgJbJVrC4+OKLtX379nrrvvzyS3Xv3t1oUwAAID7ZChb33nuv1q1bp8cff1w7d+7Uq6++qtmzZ6uoqMip/gAAQByxFSwGDBigZcuW6bXXXlNubq4ee+wxzZo1SzfddJNT/QEAgDhi+7HpI0eO1MiRI53oBQAAxDmeFQIAAIwhWAAAAGNs3cfChFP9HiwAAGg+HLmPBQAAwMkQLAAAgDEECwAAYAzBAgAAGEOwAAAAxhAsAACAMQQLAABgDMECAAAYQ7AAAADGECwAAIAxBAsAAGAMwQIAABhDsAAAAMYQLAAAgDEECwAAYAzBAgAAGEOwAAAAxhAsAACAMUluFc6dXqYEb5pb5V2xO3WsY+/dJ6ubY+/dFIsDtT86pte2ihh0AgCIBWYsAACAMQQLAABgDMECAAAYQ7AAAADG2AoWDz/8sDweT72lc+fOTvUGAADijO1vhfTu3Vvvvfde5HViYqLRhgAAQPyyHSySkpKYpQAAAA2yfY3Fjh071KVLF2VlZemGG27QV199ddLx4XBYoVCo3gIAAFomW8HiJz/5iV566SWVlZVpzpw5qq6u1uDBg/XNN980uk0gEJDP54ssfr+/yU0DAIDmyVawKCgo0JgxY9SnTx+NGDFCb7/9tiRp/vz5jW5TXFysYDAYWSorK5vWMQAAaLaadEvv1q1bq0+fPtqxY0ejY7xer7xeb1PKAACAONGk+1iEw2FVVFQoMzPTVD8AACCO2QoWv/zlL7Vq1Srt2rVLn3zyia655hqFQiEVFhY61R8AAIgjtk6F/POf/9SNN96ogwcPqkOHDho4cKDWrVun7t27O9UfAACII7aCxcKFC53qAwAAtAA8KwQAABhDsAAAAMZ4LMuyYlkwFArJ5/MpGAwqIyMjlqUBAECUTvXzmxkLAABgDMECAAAYQ7AAAADGECwAAIAxBAsAAGAMwQIAABhDsAAAAMYQLAAAgDEECwAAYAzBAgAAGEOwAAAAxhAsAACAMQQLAABgDMECAAAYQ7AAAADGECwAAIAxBAsAAGAMwQIAABiT5Fbh3OllSvCmuVUeiKndqWPdbgGnqT5Z3dxuoVlaHKiNWa1e2ypiVqs5YMYCAAAYQ7AAAADGECwAAIAxBAsAAGBMk4JFIBCQx+PRlClTDLUDAADiWdTBYv369Zo9e7b69u1rsh8AABDHogoWR44c0U033aQ5c+aobdu2pnsCAABxKqpgUVRUpKuvvlojRoz40bHhcFihUKjeAgAAWibbN8hauHChNm3apPXr15/S+EAgoEceecR2YwAAIP7YmrGorKzUPffcowULFig1NfWUtikuLlYwGIwslZWVUTUKAACaP1szFhs3btSBAweUl5cXWVdXV6fVq1fr2WefVTgcVmJiYr1tvF6vvF6vmW4BAECzZitYDB8+XFu2bKm3bvz48crJydH9999/QqgAAACnF1vBIj09Xbm5ufXWtW7dWu3btz9hPQAAOP1w500AAGBMkx+bvnLlSgNtAACAloAZCwAAYAzBAgAAGOOxLMuKZcFQKCSfz6dgMKiMjIxYlgYAAFE61c9vZiwAAIAxBAsAAGAMwQIAABhDsAAAAMYQLAAAgDEECwAAYAzBAgAAGEOwAAAAxhAsAACAMQQLAABgDMECAAAYQ7AAAADGECwAAIAxBAsAAGAMwQIAABhDsAAAAMYQLAAAgDEECwAAYEySW4Vzp5cpwZvmVvm4tDt1bJO275PVzVAnaKrFgVq3W0AT9dpW4XYLQLPEjAUAADCGYAEAAIwhWAAAAGMIFgAAwBhbwaKkpER9+/ZVRkaGMjIyNGjQIL3zzjtO9QYAAOKMrWDRtWtXPfHEE9qwYYM2bNigyy67TKNHj9bf//53p/oDAABxxNbXTUeNGlXv9YwZM1RSUqJ169apd+/eRhsDAADxJ+r7WNTV1en1119XTU2NBg0a1Oi4cDiscDgceR0KhaItCQAAmjnbF29u2bJFZ5xxhrxeryZMmKBly5bpvPPOa3R8IBCQz+eLLH6/v0kNAwCA5st2sMjOztbmzZu1bt063XXXXSosLNTWrVsbHV9cXKxgMBhZKisrm9QwAABovmyfCklJSVHPnj0lSf3799f69ev1hz/8QX/6058aHO/1euX1epvWJQAAiAtNvo+FZVn1rqEAAACnL1szFg888IAKCgrk9/t1+PBhLVy4UCtXrtTy5cud6g8AAMQRW8HiX//6l2655RZVVVXJ5/Opb9++Wr58uS6//HKn+gMAAHHEVrAoLS11qg8AANAC8KwQAABgDMECAAAY47Esy4plwVAoJJ/Pp2AwqIyMjFiWBgAAUTrVz29mLAAAgDEECwAAYAzBAgAAGEOwAAAAxhAsAACAMQQLAABgDMECAAAYQ7AAAADGECwAAIAxBAsAAGAMwQIAABhDsAAAAMYQLAAAgDEECwAAYAzBAgAAGEOwAAAAxhAsAACAMQQLAABgTJJbhXOnlynBm+ZWebhsd+pYt1s47fXJ6uZ2CzBscaDW7RYiem2rcLsFuIQZCwAAYAzBAgAAGEOwAAAAxhAsAACAMbYu3gwEAlq6dKm2bdumVq1aafDgwZo5c6ays7Od6g8AANfV1dXphx9+cLsNRyUnJysxMbHJ72MrWKxatUpFRUUaMGCAamtr9eCDDyo/P19bt25V69atm9wMAADNiWVZqq6u1rfffut2KzHRpk0bde7cWR6PJ+r3sBUsli9fXu/13Llz1bFjR23cuFGXXHJJ1E0AANAcHQ8VHTt2VFpaWpM+cJszy7L03Xff6cCBA5KkzMzMqN+rSfexCAaDkqR27do1OiYcDiscDkdeh0KhppQEACAm6urqIqGiffv2brfjuFatWkmSDhw4oI4dO0Z9WiTqizcty9LUqVM1ZMgQ5ebmNjouEAjI5/NFFr/fH21JAABi5vg1FWlpp8/NHI//rk25niTqYDFp0iR9/vnneu211046rri4WMFgMLJUVlZGWxIAgJhrqac/GmLid43qVMjkyZP15ptvavXq1eratetJx3q9Xnm93qiaAwAA8cVWsLAsS5MnT9ayZcu0cuVKZWVlOdUXAACIQ7aCRVFRkV599VX95S9/UXp6uqqrqyVJPp8vctEHAAAtWY9pb8e03u4nro5qu7Vr12ro0KG6/PLLT/hWp5NsXWNRUlKiYDCoSy+9VJmZmZFl0aJFTvUHAACi8OKLL2ry5Mlas2aN9u7dG7O6tk+FAACA5q2mpkaLFy/W+vXrVV1drXnz5umhhx6KSW2eFQIAQAuzaNEiZWdnKzs7WzfffLPmzp0bs8kBggUAAC1MaWmpbr75ZknSlVdeqSNHjuj999+PSe0m3XmzKb545AplZGS4VR6uC7rdwGlvi9sNwLxCtxtAc7B9+3Z9+umnWrp0qSQpKSlJ119/vV588UWNGDHC8fquBQsAAGBeaWmpamtrddZZZ0XWWZal5ORkHTp0SG3btnW0PqdCAABoIWpra/XSSy/pd7/7nTZv3hxZPvvsM3Xv3l2vvPKK4z0wYwEAQAvx1ltv6dChQ7r99tvl8/nq/eyaa65RaWmpJk2a5GgPzFgAANBClJaWasSIESeECkkaM2aMNm/erE2bNjnaAzMWAADYEO2dMGPhr3/9a6M/u/DCC2PylVNmLAAAgDEECwAAYAzBAgAAGEOwAAAAxhAsAACAMQQLAABgDMECAAAYQ7AAAADGECwAAIAxBAsAAGAMt/QGAMCOh098Doez9YK2Nxk3bpzmz58fed2uXTsNGDBATz75pPr27WuyuxMwYwEAQAt05ZVXqqqqSlVVVXr//feVlJSkkSNHOl6XYAEAQAvk9XrVuXNnde7cWeeff77uv/9+VVZW6uuvv3a0rmunQnKnlynBm+ZWeZzE7tSxbrcARK1PVje3W4griwO1brfQbB3LzFTdrx/Uf374QVbCf/8f3srFnqJ15MgRvfLKK+rZs6fat2/vaC2usQAAoAV66623dMYZZ0iSampqlJmZqbfeeksJCc6erOBUCAAALdCwYcO0efNmbd68WZ988ony8/NVUFCgPXv2OFqXGQsAAFqg1q1bq2fPnpHXeXl58vl8mjNnjn772986VpcZCwAATgMej0cJCQn6/vvvHa1jO1isXr1ao0aNUpcuXeTxePTGG2840BYAAGiKcDis6upqVVdXq6KiQpMnT9aRI0c0atQoR+vaPhVSU1Ojfv36afz48RozZowTPQEAgCZavny5MjMzJUnp6enKycnR66+/rksvvdTRuraDRUFBgQoKCpzoBQCAZu/7a/4vpvWi+XrrvHnzNG/ePNOtnBLHL94Mh8MKh8OR16FQyOmSAADAJY5fvBkIBOTz+SKL3+93uiQAAHCJ48GiuLhYwWAwslRWVjpdEgAAuMTxUyFer1der9fpMgAAoBngPhYAAMAY2zMWR44c0c6dOyOvd+3apc2bN6tdu3bq1o2H/wAAcDqzHSw2bNigYcOGRV5PnTpVklRYWOjaV1sAAEDzYDtYXHrppbIsy4leAABAnOMaCwAAYAzBAgAAGOPaY9O/eOQKZWRkuFUeJxV0uwEgalvcbiDeFLrdQPP1n//8R7t27VJqVpZSU1Mj6/vM7xPTPrbkRvevurq6WjNmzNDbb7+tffv2qWPHjjr//PM1ZcoUDR8+3HCX/+VasAAAAM7YvXu3Lr74YrVp00ZPPvmk+vbtqx9++EFlZWUqKirStm3bHKtNsAAAoIWZOHGiPB6PPv30U7Vu3Tqyvnfv3rrtttscrc01FgAAtCD//ve/tXz5chUVFdULFce1adPG0foECwAAWpCdO3fKsizl5OS4Up9gAQBAC3L8XlMej8eV+gQLAABakHPPPVcej0cVFRWu1CdYAADQgrRr105XXHGFnnvuOdXU1Jzw82+//dbR+gQLAABamOeff151dXW66KKLtGTJEu3YsUMVFRV65plnNGjQIEdr83VTAABamKysLG3atEkzZszQL37xC1VVValD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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.plot.barh(stacked=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 239,
   "id": "08b17a08-b7e8-48ca-9bae-183fe09629d0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='Frequency'>"
      ]
     },
     "execution_count": 239,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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XK3AzA4AADA1wg4AAGhTp06d0uOPP64uXbqoa9eu+rd/+ze/vh+LsAMAANpUUVGRgoOD9b//+7968cUXNWfOHP35z3/22/lYswMAANqU3W7XnDlzZLFYdOWVV2rnzp2aM2eOxo8f75fzMbMDAADa1PXXXy+LxeLev+GGG1RWVqampia/nI+wAwAATI2wAwAA2tTmzZtb7CcnJysoKMgv5yPsAACANrV//37l5ORoz549WrFihebNm6dJkyb57XwsUAYAAG1qzJgxOnHihK677joFBQVp4sSJevjhh/12PsIOAABmEuBPNS4pKXH/eeHChW1yTi5jAQAAU2NmBziP1KJUo0sAALQCMzsAAMDUCDsAAMDUCDsAAMDUCDsAAMDUCDsAAMDUCDsAAMDUCDsAAMDUDA07GzZs0LBhw5SQkCCLxaI1a9Z4HLdYLGfcZs+e7e6TlpbW4vioUaPa+JsAAIBAZehDBevr63X11VfrgQce0N13393ieFVVlcf+O++8o6ysrBZ9x48fr6efftq9HxYW5p+CAQAIcG35INSdY3e22blaw9Cwk5mZqczMzLMet9lsHvtvvfWW0tPT9S//8i8e7eHh4S36AgAASO1ozc53332ntWvXKisrq8Wx1157TTExMerVq5dyc3N17Nixc47ldDrlcDg8NgAA4H/Nzc169tlndcUVV8hqtap79+7605/+5Ndztpt3YxUVFSkiIkIjRozwaL/vvvuUlJQkm82mXbt2KS8vT59++qmKi4vPOlZ+fr5mzJjh75IBAMBP5OXl6ZVXXtGcOXM0YMAAVVVV6csvv/TrOdtN2Pmv//ov3XffferUqZNH+/jx491/TklJUXJysvr27avt27erd+/eZxwrLy9POTk57n2HwyG73e6fwgEAgCTp2LFjeuGFFzR//nyNHTtWknT55ZdrwIABfj1vuwg7H3/8sfbs2aNVq1adt2/v3r0VEhKisrKys4Ydq9Uqq9Xq6zIBAMA5fPHFF3I6nRo4cGCbnrddrNlZvHix+vTpo6uvvvq8fXfv3q3GxkbFx8e3QWUAAOBCGXW3tKFhp66uTjt27NCOHTskSeXl5dqxY4cqKyvdfRwOh15//XU99NBDLT6/d+9ePf3009q6dasqKiq0bt063XPPPbr22mt14403ttXXAAAAFyA5OVlhYWH68MMP2/S8hl7G2rp1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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':\n",
    "np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])\n",
    "\n",
    "df.plot.hist(bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5c6c1e8c-bf88-4dde-a653-725bf2ff1852",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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g4Omyws7N56nhl8HDhwwXVZAhcRy8KHu0qVL+pd/+Rf95je/UVdXl/bt26fvfve7pssKSzabTXPnzpUkzZ07V88//7z++q//WufOnVNSUpLh6sJLaWmpLBaL3n//fcXFxY2033XXXXr22WcNVhZ+bvy9mD9/vu69917l5ubqoYce0r59+7R+/XrDFYaXGz+PcMHIyBSora3VokWLtGjRIn3jG9/QT3/60y99nDICr7+/X/v371dmZqbmzJljupyw8qc//UlHjhzRc8895xVEhs2cOXPqi4KXBx98UHfffbfq6upMl4IwQBiZAnv37tU3vvENSdeG3/r7+5kTN6S+vl52u112u10zZszQ22+/rdra2ps+TRKT7/Tp0/J4PLrzzjtNl4KbuPPOO9XR0WG6jLBz43lq+PWDH/zAdFkBxTRNgP3hD3/Q+++/P/J/F5GRkSouLlZNTY0efvhhw9WFn/z8fO3Zs0fStf873717t1asWKH3339fCxcuNFxd+BgeGbRYLIYrwc14PB4+IwNuPE8Nmz17tqFqpgZhJMD27t2rwcFBzZ8/f6TN4/EoKipKFy5c0KxZswxWF37i4uKUmZk58nN2drYSEhL0T//0T3rppZcMVhZe7rjjDlksFrW2tmrVqlWmy8E4Wltb5XA4TJcRdr54ngoHjE0H0ODgoN58803t3LlTzc3NI6/f/e53Wrhwofbv32+6xLBnsVgUERGhy5cvmy4lrMyePVuPPvqoXnvtNV26dGnU+3/+85+nvih4+dWvfqVTp07pySefNF0KwgAjIwFUX1+vCxcuaN26dUpISPB6r6ioSHv37tW3v/1tQ9WFp4GBAXV1dUmSLly4oFdffVX9/f1auXKl4crCz+7du5WXl6f77rtP27Zt01e+8hUNDg6qoaFBe/bsUWtrq+kSw8bw74Xb7dZnn32mI0eOqKqqSoWFhVq7dq3p8sLOjeepYZGRkUpMTDRUUeARRgJo7969evjhh0cFEUl68skntX37dv32t7/Vvffea6C68HTkyBGlpqZKkmbMmKE777xTb731lpYvX262sDDkcDj029/+Vn//93+viooKuVwuJSUlKTs7e9R8OQJr+PciMjJSs2bN0t13360f/ehHevrpp7m424Abz1PDFi1apP/5n/8xVFHgWTzcYwoAAAwi8gIAAKMIIwAAwCjCCAAAMIowAgAAjCKMAAAAowgjAADAKMIIAAAwijACAACMIowAAACjCCMAAMAowggAADCKMAIAAIz6fwpjfPPQn9pUAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])\n",
    "df.plot.box()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "cbb720ba-334f-4180-a646-de8d2543aa88",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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2vqttTd66aWXyM7ObnoeCAQ4d+4cMTExHb586ErV1dUkJSVx6tQpoqOjO+115cbpmHQvOh7di45H96LjcW3GGGpqaoiPj7/qeu0KIwMGDMDpdLboBTl79myL3o9GcXFxra4fFhZGTExMq9u43W7cbneztptuuqk9pbZLdHS0/iF1Mzom3YuOR/ei49G96Hhc3dV6RBq1awCry+UiPT2dwsLCZu2FhYWMHz++1W3GjRvXYv3t27eTkZHR6ngRERERCS3tvpomOzub9957j/Xr13P48GEWLFjAyZMnmT17NnD5FMszzzzTtP7s2bM5ceIE2dnZHD58mPXr11NQUMDChQs7by9ERESkx2r3mJHHHnuM3377jaVLl1JWVsbo0aPZtm0bQ4YMAaCsrKzZnCMpKSls27aNBQsWsHr1auLj43n77beZPn165+3FDXK73bzyyistTgmJfXRMuhcdj+5Fx6N70fHoPJa51vU2IiIiIl2oe99GUERERP70FEZERETEVgojIiIiYiuFEREREbFVSIeRNWvWkJKSQkREBOnp6ezevdvukkJSbm4ut99+O1FRUQwaNIhp06Zx5MgRu8uSBrm5uViWRVZWlt2lhLTTp0/z1FNPERMTQ2RkJGlpaRQXF9tdVkjy+Xy8/PLLpKSk0KtXL1JTU1m6dCmBQMDu0nqskA0jmzZtIisri5ycHEpKSpg0aRJTpkxpdlmyBEdRURFz5sxh3759FBYW4vP5yMzMpK6uzu7SQt6BAwfIz8/ntttus7uUkHb+/HkmTJhAeHg4n3/+OYcOHeKtt97q0pmppW2vv/4669atY9WqVRw+fJg33niDFStW8M4779hdWo8Vspf23nHHHYwdO5a1a9c2tY0YMYJp06aRm5trY2VSUVHBoEGDKCoq4s4777S7nJBVW1vL2LFjWbNmDa+99hppaWnk5eXZXVZIWrx4MV999ZV6b7uJBx54gNjYWAoKCprapk+fTmRkJBs2bLCxsp4rJHtGPB4PxcXFZGZmNmvPzMxk7969NlUljaqqqgDo37+/zZWEtjlz5nD//fdzzz332F1KyNu6dSsZGRk88sgjDBo0iDFjxvDuu+/aXVbImjhxIl988QWlpaUAfPvtt+zZs4epU6faXFnPdUN37e3pKisr8fv9LW7uFxsb2+KmfhJcxhiys7OZOHEio0ePtruckPXxxx/zzTffcODAAbtLEeD48eOsXbuW7OxslixZwv79+5k3bx5ut7vZ7TckOF588UWqqqoYPnw4TqcTv9/PsmXLeOKJJ+wurccKyTDSyLKsZs+NMS3aJLjmzp3Ld999x549e+wuJWSdOnWK+fPns337diIiIuwuR4BAIEBGRgbLly8HYMyYMfzwww+sXbtWYcQGmzZt4qOPPmLjxo2MGjWKgwcPkpWVRXx8PM8++6zd5fVIIRlGBgwYgNPpbNELcvbs2Ra9JRI8zz//PFu3bmXXrl0kJibaXU7IKi4u5uzZs6Snpze1+f1+du3axapVq6ivr8fpdNpYYegZPHgwI0eObNY2YsQINm/ebFNFoW3RokUsXryYxx9/HIBbb72VEydOkJubqzByg0JyzIjL5SI9PZ3CwsJm7YWFhYwfP96mqkKXMYa5c+eyZcsWduzYQUpKit0lhbS7776b77//noMHDzY9MjIyePLJJzl48KCCiA0mTJjQ4nL30tLSphuUSnBduHABh6P516fT6dSlvR0Qkj0jANnZ2Tz99NNkZGQwbtw48vPzOXnyJLNnz7a7tJAzZ84cNm7cyKeffkpUVFRTj1Xfvn3p1auXzdWFnqioqBbjdXr37k1MTIzG8dhkwYIFjB8/nuXLl/Poo4+yf/9+8vPzyc/Pt7u0kPTggw+ybNkykpOTGTVqFCUlJaxcuZIZM2bYXVrPZULY6tWrzZAhQ4zL5TJjx441RUVFdpcUkoBWH++//77dpUmDyZMnm/nz59tdRkj77LPPzOjRo43b7TbDhw83+fn5dpcUsqqrq838+fNNcnKyiYiIMKmpqSYnJ8fU19fbXVqPFbLzjIiIiEj3EJJjRkRERKT7UBgRERERWymMiIiIiK0URkRERMRWCiMiIiJiK4URERERsZXCiIiIiNhKYURERERspTAiIiIitlIYEREREVspjIiIiIitFEZERETEVv8PYr0xoSA9uVUAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])\n",
    "df.plot.area()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "53897356-ad5d-49d2-a11e-a1a62fef82b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: xlabel='a', ylabel='b'>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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fB08eFBbtmzRK6+8onnz5unll1/WX/7lX9r1FAAAgMPYWufGDtS5AQDAfVxR5wYAACAeCDcAAMAohBsAAGAUwg0AADAK4QYAABiFcAMAAIxi+9lSiTa6853TwQEAcI/R9+1IKth4Ltz09vZKEodnAgDgQr29vfL7/VNe47kifiMjI7p06ZJuu+22KU8fHzV6ivjFixcp+ucw3Btn4r44F/fGubg3N2dZlnp7ezVv3jwlJU29qsZzIzdJSUmaP39+1I/LysrifziH4t44E/fFubg3zsW9mdrNRmxGsaAYAAAYhXADAACMQri5ibS0ND333HNKS0uzuysYh3vjTNwX5+LeOBf3JrY8t6AYAACYjZEbAABgFMINAAAwCuEGAAAYhXADAACMQriRtHPnTuXn5ys9PV1FRUU6duzYlNcfOXJERUVFSk9P16JFi/SLX/wiQT31lmjuyzvvvKMHHnhAOTk5ysrK0qpVq/Sb3/wmgb31lmh/Z0Y1NDQoJSVFX/3qV+PbQQ+L9t4MDg5q+/btysvLU1pamu666y7t3bs3Qb31lmjvzf79+3XPPfcoIyNDc+fO1RNPPKGurq4E9dblLI/71a9+Zc2aNct6/fXXrVOnTllPPfWUlZmZaV24cCHs9a2trVZGRob11FNPWadOnbJef/11a9asWdbbb7+d4J6bLdr78tRTT1k/+clPrA8++MD69NNPrW3btlmzZs2y/uu//ivBPTdftPdm1NWrV61FixZZZWVl1j333JOYznrMdO7Nt7/9bWvlypVWfX29de7cOes///M/rYaGhgT22huivTfHjh2zkpKSrJ///OdWa2urdezYMevLX/6ytX79+gT33J08H26Ki4utysrKkLYvfvGL1tatW8Ne/7d/+7fWF7/4xZC273//+9a9994btz56UbT3JZwvfelL1vPPPx/rrnnedO/Nhg0brH/4h3+wnnvuOcJNnER7b/793//d8vv9VldXVyK652nR3puf/exn1qJFi0LaXn75ZWv+/Plx66NJPD0tNTQ0pMbGRpWVlYW0l5WV6cSJE2Ef8/7770+4/pvf/KZOnjypzz//PG599ZLp3JfxRkZG1Nvbq9mzZ8eji5413Xvzxhtv6OzZs3ruuefi3UXPms69effdd7VixQr99Kc/1Z133qm7775bTz/9tP74xz8mosueMZ17U1JSos8++0wHDx6UZVn6wx/+oLffflsPPvhgIrrsep47OPNGwWBQw8PDys3NDWnPzc3V5cuXwz7m8uXLYa+/du2agsGg5s6dG7f+esV07st4L774ovr7+/Xwww/Ho4ueNZ17c+bMGW3dulXHjh1TSoqnX3Liajr3prW1VcePH1d6erp+/etfKxgM6gc/+IGuXLnCupsYms69KSkp0f79+7Vhwwb9z//8j65du6Zvf/vbqq2tTUSXXc/TIzejfD5fyJ8ty5rQdrPrw7VjZqK9L6Pq6ur04x//WAcOHNCcOXPi1T1Pi/TeDA8P65FHHtHzzz+vu+++O1Hd87Rofm9GRkbk8/m0f/9+FRcX61vf+pZeeukl/fKXv2T0Jg6iuTenTp1SVVWVnn32WTU2Nuq9997TuXPnVFlZmYiuup6nP0YFAgElJydPSM4dHR0TEvaoO+64I+z1KSkpys7OjltfvWQ692XUgQMHVFFRobfeekv3339/PLvpSdHem97eXp08eVJNTU360Y9+JOn6G6plWUpJSdGhQ4e0du3ahPTddNP5vZk7d67uvPNO+f3+sbalS5fKsix99tlnKigoiGufvWI696ampkalpaV65plnJElf+cpXlJmZqdWrV+uFF15gluAmPD1yk5qaqqKiItXX14e019fXq6SkJOxjVq1aNeH6Q4cOacWKFZo1a1bc+uol07kv0vURm8cff1xvvvkm89JxEu29ycrK0kcffaTm5uaxr8rKSi1ZskTNzc1auXJlorpuvOn83pSWlurSpUvq6+sba/v000+VlJSk+fPnx7W/XjKdezMwMKCkpNC36OTkZEn/O1uAKdi1ktkpRrfn7dmzxzp16pS1efNmKzMz0zp//rxlWZa1detW69FHHx27fnQr+JYtW6xTp05Ze/bsYSt4HER7X958800rJSXFeuWVV6z29vaxr6tXr9r1FIwV7b0Zj91S8RPtvent7bXmz59vfec737E+/vhj68iRI1ZBQYH15JNP2vUUjBXtvXnjjTeslJQUa+fOndbZs2et48ePWytWrLCKi4vtegqu4vlwY1mW9corr1h5eXlWamqqtXz5cuvIkSNj33vsscesr3/96yHX//a3v7WWLVtmpaamWgsXLrR27dqV4B57QzT35etf/7olacLXY489lviOe0C0vzM3ItzEV7T35vTp09b9999v3XLLLdb8+fOt6upqa2BgIMG99oZo783LL79sfelLX7JuueUWa+7cudb3vvc967PPPktwr93JZ1mMbwEAAHN4es0NAAAwD+EGAAAYhXADAACMQrgBAABGIdwAAACjEG4AAIBRCDcAAMAohBsAAGAUwg0AADAK4QYAABiFcAMAAIxCuAFghPfee09f+9rXdPvttys7O1t//ud/rrNnz9rdLQA2INwAMEJ/f7+qq6v14Ycf6j/+4z+UlJSkv/iLv9DIyIjdXQOQYJwKDsBInZ2dmjNnjj766CMVFhba3R0ACcTIDQAjnD17Vo888ogWLVqkrKws5efnS5La2tps7hmAREuxuwMAEAsPPfSQFixYoNdff13z5s3TyMiICgsLNTQ0ZHfXACQY4QaA63V1den06dN69dVXtXr1aknS8ePHbe4VALsQbgC43he+8AVlZ2frtdde09y5c9XW1qatW7fa3S0ANmHNDQDXS0pK0q9+9Ss1NjaqsLBQW7Zs0c9+9jO7uwXAJuyWAgAARmHkBgAAGIVwAwAAjEK4AQAARiHcAAAAoxBuAACAUQg3AADAKIQbAABgFMINAAAwCuEGAAAYhXADAACMQrgBAABG+X+HfT/MLvN1zAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])\n",
    "df.plot.scatter(x='a', y='b')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "15abaee4-4560-4776-bf80-3e65d14f012f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([<Axes: ylabel='x'>], dtype=object)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZkAAAGFCAYAAAAvsY4uAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAynklEQVR4nO3deXwU9f0/8Nee2dx3IBDCbQDDbUVEEBGs1qNFam2r9cIDlVJFwRNqf4pKUfFAKaeiKBZvRYp8pZwqCuFOAkg4whFISLKbO3vN748gRQyQZGf2vTP7ej4e+4gJMPMKkrzy+XxmPmNSFEUBERGRBszSAYiIyLhYMkREpBmWDBERaYYlQ0REmmHJEBGRZlgyRESkGZYMERFphiVDRESaYckQEZFmWDJERKQZlgwREWmGJUNERJphyRARkWZYMkREpBmrdAAiIj3y+XzweDzSMTRhs9lgsVhUORZLhoioGRRFwdGjR+F0OqWjaCohIQGtW7eGyWQK6DgsGSKiZvipYNLS0hAVFRXwN+FQoygKampqUFxcDABIT08P6HgsGSKiJvL5fCcLJjk5WTqOZiIjIwEAxcXFSEtLC2jqjAv/RERN9NMaTFRUlHAS7f30OQa67sSSISJqJqNNkTVGrc+RJUNERJphyRARkWa48E9EpIIOj34Z1PPtf/7qoJ6vpTiSISIizbBkiIhIMywZIqIwsWzZMlxyySVISEhAcnIyrrnmGhQUFGh6TpYMEVGYqK6uxvjx47FhwwasWLECZrMZI0eOhN/v1+ycXPgnIgoTo0aN+tn78+bNQ1paGvLy8pCdna3JOTmSISIKEwUFBfjzn/+MTp06IS4uDh07dgQAFBYWanZOjmSIiMLEtddei3bt2mHOnDlo06YN/H4/srOz4Xa7NTsnS4aIKAyUlpYiPz8fs2bNwuDBgwEA69at0/y8LBkiojCQmJiI5ORkzJ49G+np6SgsLMSjjz6q+XlZMkREKgj1O/DNZjPef/99jBs3DtnZ2cjKysKrr76KoUOHanpelgwRUZgYPnw48vLyfvYxRVE0PSevLiMiIs2wZIiISDMsGSIi0gxLhoiINMOSISIizbBkiIhIMywZIiLSDEuGiIg0w5IhIgoDQ4cOxQMPPBD08/KOfyIiNTwVH+TzuYJ7vhbiSIaIiDTDkQzRWSiKggp3BUprS9Gq6jiiq0uBOhdQV3HirRNwVwNQAJMFMJkB84m3P71Ovn/Kr9tjgJg0IKbViVcaEJkg/NmS0Xm9XowdOxYLFy6ExWLBvffei6effhomk0mzc7JkKOwV1xTjQMUB7K/YjwOuAzhQeQBHq4+itLYU5fXl8Pq9AIDXzRkYUvCtdkGsDiA67ZTySQNiWze8jcsA0roBCZnanZ8Mb8GCBRg9ejS+//57bNy4EXfffTfat2+Pu+66S7NzsmQoLHj8Huwu340CZwEOVBw4+SqsKESNt6ZJx3DZHdqG9NYBrsKG15k44oG0HkCr80+8shvej4jRNhsZQrt27TB9+nSYTCZkZWVh+/btmD59OkuGqLmKa4qxtWQrthZvxbbj25BXmod6X31Axyy32lVKF4A6F1D4XcPrJBOQ2L6hcH4qn9Y9gaROYjEpNF100UU/mxobOHAgXnzxRfh8PlgsFk3OyZIh3XP73MgrzcPWkq3YVrINW0u24ljNMdXP49ToizBwClC+v+G1c8n/PhyXAXQaCnS+rOFtdIpMPAprLBnSpSNVR7Dm0BqsPrQaG45uCHiU0hQuvV2LWXEI2LKw4QVTw0in89CGwmk/CLBFCgekYFu/fv0v3u/atatmoxiAJUM64fP7sLVk68li2ePcE/QM5fAH/ZzqUYBj2xte374GWCKAdheeGOVcBqT3Acx6a1FqroMHD2L8+PG45557sGnTJrz22mt48cUXNT0nS4ZCVoW7AusOrcOaw2vwzeFv4Kx3iuZx+T2i51eVrx7Yv7bhteL/AVHJwPkjgV43NpSPDg0dOhR9+vTByy+/LB0lZN1yyy2ora3FhRdeCIvFgr/+9a+4++67NT0nS4ZCitfvxdpDa/FZwWdYc2gNPCH0jd3pq5OOoJ2aUmDD3IZXYkeg1x8aCie5s3Qy/QjxO/BXrVp18r9nzpwZtPOyZCgk7CrbhU/3fIql+5airK5MOk6jnN5q6QjBUb4PWD214dW2f0PZZI/ihQPUIiwZElNWV4ale5fis4LPsLNsp3Scc3K6K6UjBN/hnIbXV48DnS9vGOF0uzpkLxqQuKOdzo4lQ0GlKArWHl6LD3d/iLWH1568m14P3H43auzRiHKHyYjmVH4v8ONXDS97LNDz98DAsUBKF+lkPyNxRzudHUuGgsLj82DJ3iVYkLsABa4C6Tgt5opOCs+SOZW7Esh5E9i0AMj6DTDobyFzsYDEHe10diwZ0lSFuwKLdy3Ge/nvoaS2RDpOwModsUiXDhEqFH/DzZ87lwDtLmoom6yrAMGpKYk72unsWDKkiaKqIryT/w4+2v1Rk/cG0wOnI1Y6Qmg6uB54fz2Qcl7DNFrvPwLWCOlUFAJYMqSqnWU78eaON7F8/3J4Ff2stzSVKyI0F7xDxvHdwBfjgJVTgAH3ABeMDuojDCTuaKezY8mQKgorCvHyppfxfwf+TzqKpkJik0w9qDrWcJPn2peA/rcBQx4GIhM1P63EHe10diwZCkhZXRlmbpmJD3/8UFdXirWUy2qTjqAv7irguxnAlneBSx8BfnUnYNHu71DijnY6O5YMtUiNpwZv572Nt3LfQrUnfK62cpp5v0WL1JYDyx5t2FFgxNNAt9+ofgqpO9rp7Fgy1Cw+vw8f7/kYM7fMNMTVYs2l700yQ0DpHuD9PwEdhwC/frbhuTcG0XNBcD+X7bduD+r5WoolQ022snAlXt70Mva69kpHEeNSQmcvNV3btwaYNQTo82dg2GQgtpV0ItII9/amcyqqKsJ9X9+HcSvHhXXBAIAzCM+tCRuKH9i8EHitH7B6GuCplU5keH6/H1OnTkWXLl0QERGBzMxMTJkyRdNzciRDZ+RX/Fi0cxFe3fSqoe51CYSTfw/qc1cBK58Bct4CrngayL5eOpFhPfbYY5gzZw6mT5+OSy65BEVFRdi5U9t9A1ky1Kg95Xvw9+/+jm0l26SjhBSnp0o6gnFVHAI+vB3Y8RFw9UucQlNZZWUlXnnlFcyYMQO33norAKBz58645JJLND0vp8voZ9w+N2ZsnoEbltzAgmlEjbcGHgvvldHUziXAGwOAre9LJzGU/Px81NfX4/LLLw/qeVkydNLm4s244YsbMGvbrLC456WlnNFJ0hGMr7Yc+OQe4L0bgYoi6TSGEBkps1sFS4ZQ663FM+ufwa3/uTXsF/abojwyXjpC+Ni9rGFUs+Mj6SS617VrV0RGRmLFihVBPS/XZMLcrrJdmLBmAva59klH0Q1XZJx0hPBS5wI+vAPYtQy4+gXAwZJvCYfDgUceeQQTJ06E3W7HoEGDUFJSgtzcXIwePVqz87Jkwti7+e/ipY0vwe13S0fRFaedm2SK2L4YKPwOGPkvoIO2i9VGNWnSJFitVkyePBlHjhxBeno6xowZo+k5TYqiKJqegUKOq96FJ9c9iVWHVklH0aVJUVn4Q66xNwINaSYzcPE44PLJgDm4uyvX1dVh37596NixIxwOR1DPHWxqfa5ckwkz20u244YvbmDBBICbZApT/MA3LwPvjARqyqTT0DmwZMLIu/nv4tZlt6KomlfrBMJp5pdNSNi3GphzGXAsTzoJnQW/WsJAjacGD69+GM//8Dw8fu69FSiniZtkhozy/cC8EUD+EukkdAYsGYM7Wn0Ut/znFny1/yvpKIbhVHzSEehU7irg3zcDq6YCXGIOOSwZA9tZthM3Lb0Ju8p3SUcxFCevxgtBCrDqWWDxLYA7fJ5vpAcsGYNac2gNbv3PrSiuKZaOYjguH3cLDln5nwPzrmiYRqOQwJIxoEU7F2Hcf8dx52SNlLsrpSPQ2RzbAcy+rOGZNSSOJWMgfsWPf274J579/ln4uG6gmUpPFXym4N6fQc1UW9ZwifPG+dJJwh5LxiBqvbV4cOWDeCfvHekohqdAQUVUgnQMOhe/F1jyIPDNq9JJwhpLxgDK6spwx7I78N+D/5WOEjbKWTL68X+TgNX/lE4RsoYOHYoHHnhAs+Nz7zKdK60txZ3L78Qe5x7pKGHF5eAmmbqycgrgrWvYikYj+d26a3bsxnTfmR/U87UURzI6drz2OEZ/NZoFI8DpiJaOQM219kVg2WPSKcIOS0anfiqYAleBdJSw5LQZe3NEw1r/RsM6TZjetFldXY1bbrkFMTExSE9Px4svvqj5OVkyOnS89jju+OoOPmBMkJObZOrXxvnAZ/cD/vDbHmjChAlYuXIlPvnkEyxfvhyrVq1CTk6OpufkmozOlNSU4I6v7sD+iv3SUcKa08Kfz3Rty7sNazQjZwOW8Pg2WFVVhXnz5uHtt9/GiBEjAAALFixARkaGpuflV4qOFNcUs2BChNMknYACtuMj4INbAW94bBNUUFAAt9uNgQMHnvxYUlISsrKyND0vS0YnimuKMfqr0SyYEOEEb3Y1hJ1LgA9vD4upM6nnU7JkdKDCXYG7l9/Nggkh3CTTQHYuAZY9Kp1Cc126dIHNZsP69etPfqy8vBy7d+/W9LzhMRmpYx6fBw+sfIBXkYUYl69OOgKp6YdZQEImcPFY6SSaiYmJwejRozFhwgQkJyejVatWeOKJJ2DW+CF8LJkQpigKnvzmSWw4ukE6Cp2m3FMlHYHUtvxJID4DOP930kk0M23aNFRVVeG6665DbGwsHnroIbhcLk3PaVKkJuronF7Z9Armbp8rHYMaYTVZsXkvLyE3HKsDuOVzIHNAo79cV1eHffv2oWPHjnA4jH2vlFqfK9dkQtSHuz9kwYQwr+JFpSNeOgapzVsHLPojUMrpabWwZELQ2kNrMWX9FOkYdA7O6ATpCKSF2jJg4Sig+rh0EkNgyYSY/NJ8PLz6YXgVr3QUOgdnJEcyhlW+D3jvD4CbD/4LFEsmhBRVFeH+FffziZY64YzgJpmGdjgH+OjOsLiHRkssmRDh8Xnw4KoHUVJbIh2Fmshpj5SOQFrb9SWw/AnpFLrGkgkR0zZOQ25prnQMagan1S4dgYJh/RtA/hc/+5A/DEY3an2OvE8mBHy1/yss2rlIOgY1k9NikY5AwfLZWCC9D+xxbWE2m3HkyBGkpqbCbrfDZDLWRnaKosDtdqOkpARmsxl2e2A/TLFkhB2oOICnvn1KOga1gIvzAOGjzgl8NBrm25aiY8eOKCoqwpEjR6RTaSoqKgqZmZkB7wjAkhFU76vHQ6seQhXvHtelchh/yoROcfB7YOUU2If/HZmZmfB6vfD5jLlRqsVigdVqVWWUxpIR9Nz3z2FX+S7pGNRCLr9HOgIF27rpQMfBMHUeBpvNBpuND687Fw74hXxR8AU++vEj6RgUAKe/XjoCBZ0CfHwPUFUsHUQ3WDIC9jr34un1T0vHoACVe6qlI5CE6mLg47sBbvvYJCyZIPP4PZi4ZiJqvbXSUShALk+ldASSsnclsO4l6RS6wJIJsnnb53EdxiDqffWotUdJxyApK58FCr+XThHyWDJBtKd8D2Zvmy0dg1TkjEqSjkBS/F7go9FAPUe0Z8OSCRK/4sffv/07PLwiyVCckXHSEUiS6yDwX+6YfjYsmSBZmLcQ245vk45BKnM6YqQjkLQfZgNFW6VThCyWTBAcrDiIGVtmSMcgDTi5JkOKD1jyIHdrPgOWjMYURcFT3z3Fq8kMymmLkI5AoeBwDpDzpnSKkMSS0diHP36IH47+IB2DNOK0ctMMOmHFP4AqPqrjdCwZDR2rPobpG6dLxyANuQy2Ay8FoM7FZ880giWjoZdyXkIlb9gztHIT5+HpFNv+DexbI50ipLBkNJJ7PBf/2fcf6RikMZfilY5AoWbJeMDrlk4RMlgyGnlh4wtQwL2NjI6bZNIvlP4IfPOKdIqQwZLRwH8L/4uNxzZKx6AgcHq5SSY1Yu0LQNk+6RQhgSWjMq/fi+k5XOwPF043HzhHjfDWAV8/JZ0iJLBkVLZ412Lsr9gvHYOCpNpbA4+ZD66iRuR9BhzLlU4hjiWjoip3Ff619V/SMSjInDHcJJMaowCrnpMOIY4lo6I52+egvL5cOgYFmTMyQToChar8JUBReO9ZyJJRSVFVEd7Nf1c6BglwOmKlI1DIUoBVz0uHEMWSUcns7bNR7+PlrOHIGREpHYFC2a4vgSNbpFOIYcmo4HjtcXy+53PpGCTEaXNIR6BQF8ZrMywZFbyT9w7cft7hG65cVl5dRuewe1nDTs1hiCUToCp3FT7Y9YF0DBLkNPPLiJogTNdm+NURoMW7F3MTzDDHTTKpSX5cDhwKv51AWDIBcPvcWJi3UDoGCXMpPukIpBcrn5VOEHRhUTJ+vx9Tp05Fly5dEBERgczMTEyZMiXg435e8DlKavmQonDn5HocNVXBCqBoq3SKoAqLknnssccwdepUTJo0CXl5eXjvvffQqlWrgI7pV/x4K/ctdQKSrjl9NdIRSE82htdjmk2Kohh6P/rKykqkpqZixowZuPPOO1U77vL9y/HQ6odUOx7pV7w9Dut27ZCOQXphjwUe2glExEgnCQrDj2Ty8/NRX1+Pyy+/XNXjLshdoOrxSL8qPVXwmwz/pURqcVcC28PnilTDf2VERqp/N3Z+aT62HQ/v/Yjof/yKHy7uX0bNkRM+U2aGL5muXbsiMjISK1asUO2YH/34kWrHImNwRidKRyA9KdoKHN4knSIorNIBtOZwOPDII49g4sSJsNvtGDRoEEpKSpCbm4vRo0c3+3i13lp8ufdLDZKSnrkccdIRSG9y3gTa9pNOoTnDlwwATJo0CVarFZMnT8aRI0eQnp6OMWPGtOhYy/YtQ5WHT0Okn3NGREtHIL3Z/hFwxRTA4D+gGP7qMrXd8p9bsLl4s3QMCjH/L7IrRuapNyVLYeI3LwAX3iWdQlOGX5NRU2FFIQuGGuWy2qUjkB7lvCWdQHMsmWb4vIDb+VPjnBZ+KVELHNsBHNwgnUJT/MpoIkVRsGTvEukYFKKcJukEpFsGv5yZJdNEG49txOGqw9IxKEQ5wU0yqYXylwBe4+5/x5JpoqX7lkpHoBDm9HukI5Be1buAvaukU2iGJdMEiqJg1cFV0jEohDl9tdIRSM/yP5NOoBmWTBPsOL4Dx2uPS8egEOb0VEtHID3buRTwG3PKlSXTBKsOrZKOQCHOxaejUiBqy4D966RTaIIl0wScKqNz8fq9qDT4ndukHcVkQXlBjnQMTYTFtjKBKKoqwu7y3dIxSAec0YmIrauQjkE6odiiUJx6MVbiV5h9tCvqNibg2xHSqdTHkjmHlQdXSkcgnXA54tBOOgSFNH9UKvYlD8GS+r6YeyQTlXtP/RZch51HK9CttbFGxCyZc+BUGTWV0xEeTzqk5nEndsWO2EFYXNkTHxxtBV/ZmVcpVuQXs2TCSbWnGhuPbZSOQTpRbnNIR6AQoJjMqErthx8iBuLN0h5YVxQPFDXtz67cWYz7L+uibcAgY8mcxbrD6+DhTXbURC5bhHQEEnL6+srewpb9wLH5oBPOGjcSooyz4SpL5izWHTbmJYWkDafFIh2Bgujs6yst4/MrWL+3FFdmp6uQMDSwZM6C2/pTc3CTTONrzvpKS+UcKGfJhIPyunIcqDggHYN0xGnyS0cglQWyvtJSGw+Ua3uCIGPJnMGW4i3SEUhnnArX74xArfWVlso9XIE6jw8OmzGmX1kyZ7ClZIt0BNIZp69OOgK10E/rK1/W98G8ovZwqbC+0lJunx/bD7vwqw5JYhnUxJI5A45kqLmc3hrpCNQM7oQu2BF7CRZXabe+0lI5B8pZMkbm8XuQW5orHYN0xuXmJpmh7BfrK0fjgaPSqRqXY6B1GZZMI/JL81Hvq5eOQTpT56tHnS0SDg+fLRMqpNdXWmoTS8bYOFVGLeWMTkJrJx/TLSmU1ldaqrTajX3Hq9ExJVo6SsD097cfBFz0p5ZyRsazZASE8vpKS+UcKGfJGNW2km3SEUinuElmcOhpfaWlcg6U4/f9M6RjBIwlc5pqTzWO1RyTjkE65bRHSkcwLL2ur7RUfpE6zyZatmwZnnnmGezYsQMWiwUDBw7EK6+8gs6dO6ty/HNhyZxmn2ufdATSMSc3yVSVPyoF+5OH4Et3X8w9os/1lZYqKK5S5TjV1dUYP348evbsierqakyePBkjR47Eli1bYDZrP60YPv/HmoglQ4FwWvglFSgjrq+0RGW9F0dddWgdH9iIbdSoUT97f968eUhLS0NeXh6ys7MDOnZT8CviNCwZCoTTzF0ym+vU9ZUFpd2x5miC4dZXWurH4sqAS6agoACTJk3C+vXrcfz4cfj9DXvsFRYWsmQk7K/YLx2BdMxpUqQj6MJP6yurcAFmH+2KgkKuZTXmx2NVGNw1NaBjXHvttWjXrh3mzJmDNm3awO/3Izs7G263W6WUZ8eSOQ1HMhQIp+KVjhCywnl9paX2Hg9sXaa0tBT5+fmYNWsWBg8eDABYty64z8ni/+VT+BU/CisKpWOQjjn93CniVFxfCcyB0sD2w0tMTERycjJmz56N9PR0FBYW4tFHH1UpXdOwZE5xuOow3P7gDCHJmMJ9k0yur6gr0JIxm814//33MW7cOGRnZyMrKwuvvvoqhg4dqk7AJmDJnIJTZRQol0edy071RLFFoSR14Mn7V7i+op4jzlp4fX5YLS0fAQ4fPhx5eXk/+5iiBG/tkCVziv2u/dIRSOeqPNXwmG2w+Y39ADOurwSH16/gUHktOuh4exn+yzhFcU2xdAQyAFd0IlIqjfdv6af1lQ+qsrH4aGuurwRJYVkNS8YoyuuNs702yXFGGaNk/re+chEWlPbg+oqQ41X6vpiEJXOKsroy6QhkAHreJJPrK6GnvEbfU68smVOU13EkQ4Fz2qOkIzQL11dCm7NG31e88l/TKTiSITU47aG/OzDXV/SjnCVjHBzJkBqcVpt0hF/4aX1lQ8RFeIvrK7rC6TKDqPHUoM5XJx2DDCBUNsnk+ooxcLrMIHhlGanFKdgxJ9dX6vtgblEHrq8YQHk1RzKGwKkyUosLwd0k053QBbmxg/BBVS/8m/uDGQ5HMgbBRX9SS7lP228KXF8JL1yTMYgqd/jtOUXacPlqVT8m11fCV63HhzqPDw6bRTpKi7BkTvApPukIZBBOT7Uqx+H6Cv3EWeNB63iWjK6xZEgtFZ5K+E1mmBV/s/+sO6EzcuMuwQeVXF+h/3F7m/9vKVSwZE7w+VkypA6/4kdFZDwSas59Mcmp6ysLSrtj9dFErq/QL/iCuDW/2lgyJ3AkQ2pyRiedsWQUayRK0hqebz/n2Hn4kesrdA4+fxiVzNdff43hw4c3+muzZs3CPffcE3AoCf4WTG0QnYnTEfuz9/1RKdifNBhfuvthbhH3B6PmCauSufrqqzF27Fg899xzsNvtAICSkhLccccd+Oabb3RbMhzJkJqcEdFcXyHVhFXJrFmzBn/5y1/w9ddf47333sP+/ftxxx13oEePHti6dasWGYOCIxlSS5YnBa2WRWNPVSYiUIibUYibpUORrrWr7gYgTjpGizS7ZAYMGIDNmzdjzJgx6N+/P/x+P5555hlMmDABJlNo7NnUEiwZUkNPdxomL/JDObID+v1qoFBj0/GFSS0av+/atQsbNmxARkYGrFYrdu7ciZqaGrWzBZXXH9ytQMh4flXfBpMXeqAc4eVhpC6TRb9Trc1O/vzzz2PgwIEYMWIEduzYgQ0bNmDz5s3o1asXvvvuOy0yBoUC/c55krxBde0wcUEVlGMl0lHIiCz6vBETaMF02SuvvIJPP/0UV111FQDg/PPPxw8//IDHH38cQ4cORX29Pp9HHWnlZaTUMpfXdsCYt0qgOF3SUcigTOFUMtu3b0dKSsrPPmaz2TBt2jRcc801qgULtlh77Ll/E9FpflPdGbe/eRhKJfe+I+2EVcmcXjCnuvTSSwMKIynGFiMdgXRmVGUW/jh/HxSdr0dS6DPH6veHYN4RdgJHMtQcf3Z1x8j5P0Kp49NUSWMWC0vGCDiSoaa6ozQbV76ZC8Wj7+d8kD5Y4uN1fXsIS+aEGDtLhs7tvpJeGPrWNsDLS94pOCwJCdIRAsKSOSHWpt/hKAXH+KN9cNGCTYCfN+5S8LBkDIIjGTqbxw71Rd+FGwEdb7lO+qT3ktHvbaQqs5qtvFeGGvWP/f3Q950NLBgSYUlMkI4QEJbMKbj4T6d7fk8/dF/0g3QMCmMcyRhIcmSydAQKIS/l9UOnD1gwJIslYyBtY9pKR6AQYFKAGdv6IuMzFgzJ03vJcOH/FBkxGdIRSJgFJryxqRcSl2+QjkIEALAmJkpHCAhL5hRtYzmSCWd2xYKZ3/dA7Moc6ShEJ9ky9P3DL0vmFJwuC18RigWz13ZD5DebpaMQ/Y/JBHv79tIpAsKSOQWny8JTjGLHzP92QsQP+n18OBmTtXVrmCP1fWsFS+YUbWLawAQTH2AWRuL9Dsxc3g7WzTukoxD9gr2DvkcxAK8u+xmH1YGUyDM/yoCMJcUfjVlL28C6OV86ClGjIjp2lI4QMJbMabguEx7SfbF4/bMUmLfvlo5CdEb2Dh2kIwSMJXMaXmFmfO29CXjl43iYdhZIRyE6KyOUDNdkTpMZmykdgTTU1ZOMZz+0Qdm/XzoK0TnZDTBdxpI5TVZilnQE0sj57jQ89W9AOXRIOgrROZlsNtja6n9mhSVzmm7J3aQjkAb6utPx+MJ6KMeKpaMQNYmtfSZMZv2vaOj/M1BZ25i2iLPHSccgFQ2sy8ATC2pYMKQrER07SUdQBUumEd2SOJoxiqG17TH+LSf8x0uloxA1S2TvXtIRVMGSaUT3pO7SEUgFV1Z3xv3ziqGUO6WjEDVbZN++0hFUwTWZRmSnZEtHoAD9tqorbp5fCKW6WjoKUbOZbDY4so3xfYgl04ieqT2lI1AA/ujqhlFv7oFSWycdhahFInp0hzkiQjqGKjhd1oi2MW2R7OBTMvXo1vLzMWrubhYM6VpUH2NMlQEsmTPiaEZ/xhzviavn5kJxu6WjEAXEKOsxAEvmjHqn9paOQM3wt2O9MWz+NsDrlY5CFLDIfsYpGa7JnMGFrS+UjkBN9Mjhvuj/zkZA4SMaSP9sbdrAlpYmHUM1HMmcQXZKNhIiEqRj0DlMPtAX/d/ewIIhwzDSVBnAkjkjs8mMi9Ivko5BZ/FsQT9kv7dBOgaRqow0VQawZM7q4jYXS0egM3hhZz90WfyDdAwi1UVfaKypeq7JnAVLJjS9tr0vWi1hwZDx2Nq1Q0TXrtIxVMWRzFm0im6FLgldpGPQCSYFmLmpD1ot4RQZGVPssMukI6iOJXMOg9oMko5AAKyKGXM29ELyVxuloxBpJmbY5dIRVMeSOYeL23LKTFqEYsGcb3ogbsUm6ShEmrHExyOqfz/pGKpjyZxD/1b94bA4pGOErSi/DXNXnYfotVukoxBpKvrSITBZjbdMzpI5hwhLBC5ofYF0jLAUrzgw5+uOiFi/XToKkeZihw2TjqAJlkwTXNH+CukIYSfZH4V//actbDl50lGINGey2RB9yWDpGJpgyTTB8PbDEWExxrbbepDmj8brX6TBsnWXdBSioIgaMACWmGjpGJpgyTRBrD0WQzKGSMcICxneeMz4JAnmvD3SUYiCJsaAly7/hCXTRFd3ulo6guF18iZi+ofRwO590lGIgsdkMux6DMCSabIhbYcgzh4nHcOwunlSMPV9O5R9hdJRiIIq6qIBsLVuLR1DMyyZJrJZbBjRfoR0DEPq5W6Fp99VoBw8LB2FKOgSfv976QiaYsk0A6fM1HdhfVtMerseStEx6ShEQWeJj0fsCGP/8MqSaYYLWl2A1tHGHdYG2+C6TEx4qwJKyXHpKEQi4q67Dma7XTqGplgyzWAymXBVx6ukYxjCFdWdMG7+cShl5dJRiMQYfaoMYMk027WdrpWOoHvXVHXBXfMPQ3FVSEchEuPo2ROOrPOkY2iOJdNMXRO7on+r/tIxdOuGiizcOvcAlKpq6ShEosJhFAOwZFrkL93/Ih1Bl2529sAf5u6BUlsrHYVIlCkqCnFXh8eFRCyZFrgs8zK0jWkrHUNX7izNxnVz86HU10tHIRIX9+tfG3YbmdOxZFrAbDLjz93+LB1DN8YW98IV87YDHo90FKKQkHBDeEyVASyZFru+6/WItoXHTyKBmFDUB0Pe3AL4fNJRiEKCo1cvRPUz3sPJzoQl00Ix9hj8tvNvpWOEtCcP9sWvFuQAfr90FKKQkXL3XdIRgoolE4Cbut8Es4l/hY15el8/9Fq4AVAU6ShEISOiaxfEXH65dIyg4nfIAGTGZWJIWz4C4HT/3N0PWe//IB2DKOQk33UXTCaTdIygYskE6OYeN0tHCCkv5/ZDh49YMESns7VrFzaXLZ+KJROgAekD0DOlp3QMcSYFeH1rX7T5nAVD1Jjk0aNhslikYwQdS0YFY/uOlY4gygITZm3sjdSlG6SjEIUka1oa4q8fKR1DBEtGBRe3uRgXtr5QOoYIu2LBnG+zkfB1jnQUopCVdNttht9t+UxYMioZ12+cdISgcyhWzFmThZjVm6WjEIUsS3w8Ev94o3QMMSwZlfRO7Y2hGUOlYwRNrD8Cc1d0QeS326SjEIW0xFv+AnNUlHQMMSwZFf2131/D4r6ZRH8kZi3PhH3DDukoRCHNmpqK5Ntuk44hyvjfEYPovMTzcGWHK6VjaCrNF4OZX6bDujlfOgpRyEt94AGYo8N7+ymWjMrG9hkLq8kqHUMTbX1xeO2zJJh37JaOQhTyHD16hO0VZadiyaisXVw7/K7r76RjqK6DNwHTP4qFadde6ShEutDqicfD7u7+xrBkNHBv73sRZTXOQl9XbzKmLXYABQekoxDpQuyVVyKqP5+gC7BkNJEWlYb7+twnHUMVPd1pePZdE5QDh6SjEOmCKSICaQ8/LB0jZLBkNHJz95vRLambdIyAXFDfBpMXeqAcOSodhUg3km67DfYMPjn3JywZjVjMFky6aJJuL2keVNcOjyyognKsRDoKkW5YU1PD7nkx56LP74A60Su1F0Z1HSUdo9mG1XTAA2+WQSktk45CpCu8ZPmXWDIae6D/A0hyJEnHaLLfVHfGvfOPQnG6pKMQ6Yqjdy9estwIlozG4uxxePgCfSwCXl95Hm6fexBKZZV0FCJdMdntaPPss7xkuREsmSC4tvO1GNB6gHSMs/qTqzv+NHcvlJoa6ShEupNy332I6NxZOkZIYskEyZMXPQm7OTS3+r697HyMnLMTSl2ddBQi3XH06IHkO0dLxwhZLJkg6RDfAWN6j5GO8Qv3lvTCVfNyAY9HOgqR/thsSH92CkxWY24lpQaWTBCN7jka/VuFzl3ADx7tjcvmbwG8XukoRLqUet+9cHTT9/1wWjMpiqJIhwgnR6uPYtTno1DhrhDN8dihvui7cCPA//1ELRLZpw/av7sQJotFOkpI40gmyFpHt8ZTFz8lmuGp/f3Q950NLBiiFjJFRaHN1OdZME3AkhEwov0IsZs0n9vTDz0W/SBybiKjaDVxIuzt20vH0AWWjJBHLnwEHeI6BPWcL+X3Q+cPWDBEgYgZNgyJf7xROoZucE1GUH5pPm5aehM8fm2v7DIpwGvb+yLtyw2anofI6GztM9Hxww9hiY2VjqIbHMkI6p7cHX/r9zdNz2GBCTM39WHBEAXIFBWFdjNmsGCaiSUj7JYet2BQ20GaHNuqmDFrfU8kLd+oyfGJwkmbKc8gomtX6Ri6w5IRZjKZMHXwVLSPU3cRMUKxYO66HohbuUnV4xKFo6Tbb0fcVVdJx9AlrsmEiH2ufbhp6U2odFcGfKwovw2zVnVBxPfbVUhGFN6iBgxA5vx5vFy5hTiSCREd4zvihUtfgMUU2D/keMWBOV93ZMEQqcCano62019iwQSAJRNCLm5zMSb8akKL/3yyPwr/+rItbDl5KqYiCk8mux0Zr74Ka5J+ngcVilgyIeam7jfhhvNuaPafa+2LwRufp8KyfZcGqYjCT+u/T0Zkz2zpGLrHkglBjw94HBe2vrDJvz/Tl4BXP0mAKb9Aw1RE4SPp9tuRMEp/j04PRSyZEGQ1W/HS0JeQGZt5zt/b1ZOMFxdHAj/u1z4YURiIHzkSaRNbPm1NP8ery0LYXtde3Lz05jNecdbDnYp//NsE5dCRICcjMqaYYcOQ8dqrXOhXEUcyIaxTfCe8fvnriLRG/uLX+rrT8Y93fSwYIpVEXXABryTTAEsmxPVN64vpQ6fDZrad/NjAugw8saAGytFiwWRExhHRvTsyZr4Bc0SEdBTD4XSZTizfvxwT10zE4JoM3L+gFEq5UzoSkSHYMjPR4b13YU1JkY5iSCwZHVmZuwTpdzwNxSX7VE0io7CmpqL9ovdgz8iQjmJYnC7TkcvOvwatxj8EmEzSUYh0zxwXh3Zz57JgNMaS0ZnEG/+A1pMnSccg0jVzfDwyZ8+CI+s86SiGZ5UOQM2X+Kc/QfH6cGzKFOkoRLpjSUlB5ry5cGRlSUcJCywZnUr6y82AouDYc88BXFYjahJrm3S0nz8f9g4dpKOEDS7865zriyUoevxxKB5tH+FMpHf2jh2ROX8ebOnp0lHCCkvGAKq//RaH/joO/upq6ShEISmiR3dkzp3LHZUFsGQMoi4vD4X33ANfyXHpKEQhJbJfP7Sb9S9YYmOlo4QlXl1mEI4ePdBh0SLY26v7GGciPYu+5BJkzpvLghHEkjEQe0YG2r+/CI5evaSjEImLvfJKtHvjdZgjf7n3HwUPp8sMyF9Tg0MPPojq1WukoxAFn8mElLH3I+W++2DijcviWDIGpXi9KJr8d7g+/lg6ClHQmKOj0WbaPxE7bJh0FDqBJWNwZW+/g2PTpgG8xJkMzt6+PTJen4GILl2ko9ApWDJhoGbzZhx+cDy8R49KRyHSRPTgwWj74guwxMVJR6HTsGTChLesDEcefhjV334nHYVIVcl33YnUBx+EyczrmEIRSyaMKH4/Sl57DaX/msWtaEj3TJGRSH/macRffbV0FDoLlkwYqlq9GkcmPgKfyyUdhahFbJmZyHjlZTi6d5eOQufAkglT7kOHcfhvf0Ndbq50FKJmSbjxRrR6ZCLMUVHSUagJWDJhzO92o/j551G+6H1On1HIs6SmoM0zzyDm0kulo1AzsGQI1evXo+jJSfAcOiQdhahRsVdcgdb/eArWxETpKNRMLBkC0LBLQPFL01H+7rsc1VDIMMfGovWTTyD+t7+VjkItxJKhn6nJyUHR40/AfeCAdBQKc1EDBqDNc8/C1qaNdBQKAEuGfsFfV4eSV15F2YIFgN8vHYfCjMnhQOrf/oak227l3mMGwJKhM6rduhVHHn8C7oIC6SgUJmKvuAKtHpkIW9u20lFIJSwZOiu/243jb7yBsvlvQnG7peOQQdm7dEbrJ55A9MCB0lFIZSwZahLP4cMofmk6KpYu5YUBpBpzbCxSx96PxJtugslqlY5DGmDJULPUbtuGY89PRe2mTdJRSM9MJsRfPxJp48fDmpwsnYY0xJKhFqn4ajmKX3wRnsJC6SikM47evdD6yScR2bOndBQKApYMtZjidqN80SKUvDETfu6DRudgb98eKffdi7jrruNVY2GEJUMB87lcOP7GTJS/9x4UPhyNTmPv1AkpY+5B3NVXw2SxSMehIGPJkGo8x46h7K0FcC5eDH91tXQcEhbRtQuSx4xB3FVX8VkvYYwlQ6rzVVSgfNH7KHvnHfiOH5eOQ0EW0a0bUsaMQeyvr+C0GLFkSDv++nq4PvkUpW/Oh+cALxAwOsf55yPlvnsRM2wYy4VOYsmQ5hS/H5XL/w+lc+eibscO6TikJrMZMUOGIPGmmxAz+BLpNBSCWDIUVNXrv0fZO++gavVqwOuVjkMtZElMRMLvRyHhxj/CnsEtYOjMWDIkwltaCtcXX8D1yaeo37VLOg41UdQFFyDhht8j9qqrYLbbpeOQDrBkSFxtbi5cn3yKiiVL4HM6pePQaSypKUj43e8Qf/31iOjYUToO6QxLhkKG4najcuUquD75BFVr1wI+n3SksGWOj0fs0EsR++srETNkMPcVoxZjyVBI8paUoGLpUlSuXIWanByAN3lqzpqaipjhlyN2+HBEDxjAYiFVsGQo5PmqqlC97htUrV6NqjVr4CstlY5kGLbMTMSOGI7Y4cMR2acPLz0m1bFkSFcURUHd9u2oWrUaVatXoy4vj48eaA6bDZE9eiB68GDEjhgBR9Z50onI4FgypGue4mJUr1mD6vXfo3bzZngOH5aOFFJMUVGI6tMbkf37I6r/BYjs3QvmyEjpWBRGWDJkKJ5jxajdvLnhtWUL6nbtglJXJx0raCyJiYjs3w9R/S9A1AX94ejenWsrJIolQ4ameL2o37MHdbm5qN2xA3W5eXDv3Qt/VZV0tICYbDbYO3SAvUtnRHTqjIjOnRDRrRsiOnWSjtaooUOHok+fPnj55Zelo1CQ8UccMjST1QpHt25wdOuGhFGjTn7cW14OT2Eh3IUH4S48AE/hQbgPHoT7YCF8JaGzqac5Ohr2Tp0Q0akT7J1PlEnnzrC1a8dt80kXWDIUlqyJibAmJiKyd+9f/Jq/pgbugwfhOXgQ3vJy+Csq4ausOPG2Er4K1y8+ptTW/u8AZjNgsTRsb9/YW6sVloQEWJOSYElKgjU5CZak5J+/TU6GNSkJ5qioIP6tEKmPJUN0GnNUFBxZWXBkZTX5zygnbhzl6AKorq7Gvffei48//hixsbF4+OGHpSORID5JiEgFJouFBXPChAkTsHLlSnzyySdYvnw5Vq1ahZycHOlYJIQjGSJSTVVVFebNm4e3334bI0aMAAAsWLAAGRkZwslICkcyRKSagoICuN1uDBw48OTHkpKSkNWMqUcyFpYMEamGd0TQ6VgyRKSaLl26wGazYf369Sc/Vl5ejt27dwumIklckyEi1cTExGD06NGYMGECkpOT0apVKzzxxBMwm/nzbLhiyRCRqqZNm4aqqipcd911iI2NxUMPPQSXyyUdi4RwWxkiItIMx7BERKQZlgwREWmGJUNERJphyRARkWZYMkREpBmWDBERaYYlQ0REmmHJEBGRZlgyRESkGZYMERFphiVDRESaYckQEZFmWDJERKQZlgwREWmGJUNERJphyRARkWZYMkREpBmWDBERaYYlQ0REmmHJEBGRZlgyRESkGZYMERFphiVDRESaYckQEZFmWDJERKQZlgwREWmGJUNERJphyRARkWZYMkREpBmWDBERaYYlQ0REmmHJEBGRZlgyRESkGZYMERFphiVDRESaYckQEZFmWDJERKQZlgwREWnm/wN69n9mS+R/lQAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])\n",
    "df.plot.pie(subplots=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd53000d-5ada-45cc-946c-e54ec5905f69",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
