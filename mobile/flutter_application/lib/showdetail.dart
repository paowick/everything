import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';

class BookDetail extends StatefulWidget {
  final String _idi; //if you have multiple values add here
  BookDetail(this._idi, {Key? key}) : super(key: key);

  @override
  State<BookDetail> createState() => _BookDetailState();
}

class _BookDetailState extends State<BookDetail> {
  FirebaseFirestore _firestore = FirebaseFirestore.instance;
  @override
  Widget build(BuildContext context) {
    String _id = widget._idi;

    return StreamBuilder(
      stream: getBook(_id),
      builder: (context, AsyncSnapshot<QuerySnapshot> snapshot) {
        return Scaffold(
          appBar: AppBar(
            title: const Text("Detail Books"),
          ),
          body: snapshot.hasData
              ? buildBookList(snapshot.data!)
              : const Center(
                  child: CircularProgressIndicator(),
                ),
        );
      },
    );
  }

  ListView buildBookList(QuerySnapshot data) {
    return ListView.builder(
      itemCount: data.docs.length,
      itemBuilder: (BuildContext context, index) {
        var model = data.docs.elementAt(index);
        String a = model['detail'] + '  by ' + model['author'].toString();
        return ListTile(
          title: Text(model['detail']),
          subtitle: Text(a),
          trailing: ElevatedButton(
            child: const Text('Delete'),
            onPressed: () {
              print(model.id);
              deleteValue(model.id);
              Navigator.pop(context);
            },
          ),
        );
      },
    );
  }

  Future<void> deleteValue(String titleName) async {
    await _firestore
        .collection('books')
        .doc(titleName)
        .delete()
        .catchError((e) {
      print(e);
    });
  }

  Stream<QuerySnapshot> getBook(String titleName) {
    return _firestore
        .collection('books')
        .where('title', isEqualTo: titleName)
        .snapshots();
  }
}
